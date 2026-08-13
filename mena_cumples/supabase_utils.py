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


def get_supabase_client() -> Client:
    """Initializes and returns a singleton instance of the Supabase client (thread-safe)."""
    global _supabase_instance
    if _supabase_instance is None:
        with _supabase_lock:
            if _supabase_instance is None:
                supabase_url = os.getenv("SUPABASE_URL")
                supabase_key = os.getenv("SUPABASE_KEY")

                if not supabase_url or not supabase_key:
                    raise ValueError("Supabase URL and Key must be set in Environment Variables")

                _supabase_instance = create_client(supabase_url, supabase_key)

    return _supabase_instance


def reset_supabase_client() -> None:
    """Drops the cached client so a fresh one (with a new connection pool) is created."""
    global _supabase_instance
    with _supabase_lock:
        _supabase_instance = None