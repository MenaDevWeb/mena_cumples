# AGENTS.md — mena_cumples

Reflex 0.9.7 app (Python 3.12). Birthday-pack ordering site for Hotel Mena Plaza café. No tests, linter, or CI in repo.

## Run

```bash
source .venv/bin/activate   # .venv already exists, reflex installed
reflex run                  # frontend :3000, backend :8000 (see `rxconfig.py`)
```

- Env required: `SUPABASE_URL`, `SUPABASE_KEY` (copy `.env.example` → `.env`). Same Supabase project as `hotel_mena_plaza_web`.
- `mena_cumples/supabase_utils.py` calls `load_dotenv()` explicitly — Reflex does not auto-load `.env`.
- Never edit `.web/`, `.states/`, `__pycache__/` (generated). Public files in `assets/` are served at `/filename` (e.g. `assets/packs_info_image.webp` → `/packs_info_image.webp`).

## Structure

- Entry: `mena_cumples/mena_cumples.py` (`app = rx.App`, home page + layout). Routes enum: `mena_cumples/routes.py`.
- `pages/` — one file per pack (`pack_15/20/25/30`, `pack_mediodia`, `pack_selection`, `packs_information`, `contact_form_page`).
- `states/state.py` — landing state: `order_code` gate, nav menu, conditions flags.
- `states/form_state.py` — `FormBaseState`: pack forms, price calc, `send_whatsapp_message`. `states/contact_form_state.py` — availability form.
- `components/pack_form.py` — shared order form. `data/conditions.py` — shared `CONDITIONS` list. `styles/styles.py` — `Color`, `FontSize`, `Size`, etc. Use these, don't hardcode.
- `rxconfig.py` plugins: `RadixThemes`, `TailwindV3`, `Sitemap`. Styling mixes `class_name`/Tailwind with the `styles.py` tokens.

## Gotchas

- **Order-code gate is fail-closed**: `verificar_codigo_reserva()` checks `cumples_pedidos.codigo_reserva` and returns `False` on any exception. Supabase calls are blocking → always wrap with `await asyncio.to_thread(...)` (see `state.py:submit_order_code`).
- **Conditions gate lives in one place**: home (`create_conditions_section`) is informational only. Mandatory acceptance is the modal in `pages/pack_selection_page.py` (`conditions_modal` + `State.accept_conditions`). Don't add blocking gates on home.
- **Dynamic pricing**: base prices + `PRICE_INCREASE_2026 = 20` (€, applies to year ≥ 2026) live in `form_state.py` (`PACK_BASE_PRICES`, `get_pack_price`, `pack_title_with_price`). Changing a price requires updating `PACK_OPTIONS_DATA` in `pack_selection_page.py` and the display in `packs_information_page.py` too. Full spec: `.agent/workflows/precios_dinamicos.md`.
- Codes are normalized `.strip().upper()` everywhere; keep that when touching `order_code` / `codigo_reserva` flows.
- Supabase client is a thread-safe singleton; call `reset_supabase_client()` if you ever need a fresh client (e.g. key rotation in a long-lived process).
