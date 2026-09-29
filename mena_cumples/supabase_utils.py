import os
import threading
from typing import Optional
from dotenv import load_dotenv
from supabase import create_client, Client

# Carga el .env del proyecto (no sobreescribe variables ya definidas en el entorno).
# Reflex 0.9.x no lo carga automáticamente salvo que se indique REFLEX_ENV_FILE.
load_dotenv()

# Global variable to cache the Supabase client
_supabase_instance: Optional[Client] = None
_supabase_lock = threading.Lock()


def get_supabase_key() -> str:
    """Devuelve la clave de Supabase, prefiriendo service_role (solo servidor).

    DESPUÉS del cierre de RLS (migraciones 006/007 de hotel_mena_plaza_web) la
    clave anon NO ve `cumples_pedidos`: toda policy anon de esa tabla se
    borró, así que con la anon el gate de códigos devolvía siempre False y el
    cliente veía "código no válido" con un código correcto. Igual que el panel
    del hotel, este backend usa service_role (bypassa RLS).

    La clave nunca llega al navegador: todas las llamadas se hacen en el
    backend (`asyncio.to_thread`). Mantener SUPABASE_KEY como fallback solo
    para desarrollo local sin la clave de servicio.
    """
    key = os.getenv("SUPABASE_SERVICE_KEY") or os.getenv("SUPABASE_KEY")
    if not key:
        raise ValueError("SUPABASE_SERVICE_KEY or SUPABASE_KEY must be set in Environment Variables")
    return key


def uses_service_role() -> bool:
    """True si el backend corre con service_role (bypass de RLS)."""
    return bool(os.getenv("SUPABASE_SERVICE_KEY"))


def get_supabase_client() -> Client:
    """Initializes and returns a singleton instance of the Supabase client (thread-safe)."""
    global _supabase_instance
    if _supabase_instance is None:
        with _supabase_lock:
            if _supabase_instance is None:
                supabase_url = os.getenv("SUPABASE_URL")
                supabase_key = get_supabase_key()

                if not supabase_url:
                    raise ValueError("Supabase URL must be set in Environment Variables")

                _supabase_instance = create_client(supabase_url, supabase_key)

    return _supabase_instance


def verificar_codigo_reserva(codigo: str) -> bool:
    """Devuelve True si el código de reserva existe en la tabla cumples_pedidos.

    Usado por la web de cumpleaños para impedir pedidos con códigos inventados
    o que el hotel no ha emitido. Falla en modo seguro (False) si la consulta
    falla, PERO avisa al log del servidor en los dos casos silenciosos:

    - excepción de red/permisos (queda el motivo),
    - 0 filas sin excepción, que es como se manifiesta el RLS bloqueando
      (PostgREST devuelve 200 [] en vez de un error). Sin este aviso, un gate
      roto por credenciales era indistinguible de un código inexistente.
    """
    codigo = (codigo or "").strip().upper()
    if not codigo:
        return False
    try:
        client = get_supabase_client()
        response = (
            client.table("cumples_pedidos")
            .select("id")
            .eq("codigo_reserva", codigo)
            .limit(1)
            .execute()
        )
        if response.data:
            return True
        if not uses_service_role():
            print(
                f"[Cumples] El código {codigo} no existe O la clave 'anon' no puede "
                "leer cumples_pedidos (RLS). Configura SUPABASE_SERVICE_KEY para "
                "descartar RLS: sin ella el gate rechaza códigos válidos."
            )
        return False
    except Exception as e:
        role = "service_role" if uses_service_role() else "anon"
        print(
            f"[Cumples] No se pudo verificar el código {codigo} con la clave "
            f"'{role}': {e}"
        )
        return False


def reset_supabase_client() -> None:
    """Drops the cached client so a fresh one (with a new connection pool) is created."""
    global _supabase_instance
    with _supabase_lock:
        _supabase_instance = None