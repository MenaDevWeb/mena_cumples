# Cumple Mediodía Implementation Plan

> **For agentic workers:** Use `mobiai-mobile-executing-plans-with-subagents` to implement task-by-task.

**Goal:** Añadir tipo "Cumple Mediodía" (13:00-15:00) a mena_cumples con menú por cantidades + nota por producto, reutilizando extras y repostería, compatible con hotel_mena_plaza_web (detalle JSONB).

**Architecture:** Extender `FormBaseState` con `CUMPLE_TIPO_OPTIONS=["Cumple Tarde","Cumple Mediodía"]`, `MENU_MEDIODOIA_TYPES`, `PACK_MENU_MEDIODOIA_LIMITS`, `BIRTH_TIMES_MEDIODOIA=["13:00","13:30","14:00","14:30","15:00"]` / `BIRTH_TIMES_TARDE`. UI condicional `rx.cond(cumple_tipo=="Cumple Mediodía")` en `pack_form.py`. Payload Supabase con alias `turno`/`tipo_cumple`/`cumple_tipo` para compat.

**Tech Stack:** Reflex 0.9.x, Python, Supabase

**Platform:** Web Reflex (mena_cumples) + dashboard receptor (hotel_mena_plaza_web)

---

### Task 1: FormBaseState - constantes y estado mediodía

**Files:**
- Modify: `mena_cumples/states/form_state.py:1-110`

- [ ] Step 1: Añadir constantes tras PACK_DRINK_LIMITS

```python
CUMPLE_TIPO_OPTIONS = ["Cumple Tarde", "Cumple Mediodía"]
BIRTH_TIMES_TARDE = ["16:00","16:30","17:00","17:30","18:00","18:30","19:00"]
BIRTH_TIMES_MEDIODOIA = ["13:00","13:30","14:00","14:30","15:00"]
MENU_MEDIODOIA_TYPES = [
    "Nuggets de pollo con patata + 1 bebida",
    "Hamburguesa con patatas + 1 bebida",
    "Sandwich mixto con patatas + 1 bebida",
    "Pasta con tomate o aceite + 1 bebida",
]
PACK_MENU_MEDIODOIA_LIMITS = {"Pack_15":15,"Pack_20":20,"Pack_25":25,"Pack_30":30}
```

- [ ] Step 2: Añadir vars estado

```python
cumple_tipo: str = "Cumple Tarde"
menu_mediodia_selected: Dict[str,int] = {t:0 for t in MENU_MEDIODOIA_TYPES}
menu_mediodia_notes: Dict[str,str] = {t:"" for t in MENU_MEDIODOIA_TYPES}
```

- [ ] Step 3: Vars computadas limit/total/remaining + birth_times dinámico

```python
@rx.var
def menu_mediodia_limit(self) -> int:
    return PACK_MENU_MEDIODOIA_LIMITS.get(self.selected_pack, 15)
@rx.var
def menu_mediodia_total(self) -> int:
    return sum(self.menu_mediodia_selected.values())
@rx.var
def menu_mediodia_remaining(self) -> int:
    return max(0, self.menu_mediodia_limit - self.menu_mediodia_total)
@rx.var
def birth_times_options(self) -> list[str]:
    return BIRTH_TIMES_MEDIODOIA if self.cumple_tipo=="Cumple Mediodía" else BIRTH_TIMES_TARDE
```

- [ ] Step 4: Commit
`git add mena_cumples/states/form_state.py && git commit -m "feat(cumple): add Cumple Mediodía constants and state"`

---

### Task 2: FormBaseState - eventos y validación

**Files:**
- Modify: `mena_cumples/states/form_state.py:140-410`

- [ ] Step 1: Eventos set_cumple_tipo, update_menu_mediodia, update_menu_note

```python
@rx.event
def set_cumple_tipo(self, v: str):
    self.cumple_tipo = v if v in CUMPLE_TIPO_OPTIONS else "Cumple Tarde"
    if self.cumple_tipo=="Cumple Mediodía" and self.birth_time not in BIRTH_TIMES_MEDIODOIA:
        self.birth_time=""
    elif self.cumple_tipo=="Cumple Tarde" and self.birth_time not in BIRTH_TIMES_TARDE:
        self.birth_time=""

@rx.event
def update_menu_mediodia(self, menu_type: str, value: str):
    new=int(value) if str(value).isdigit() else 0
    old=self.menu_mediodia_selected.get(menu_type,0)
    tmp=dict(self.menu_mediodia_selected); tmp[menu_type]=new
    if sum(tmp.values())>self.menu_mediodia_limit:
        tmp[menu_type]=old
        self.menu_mediodia_selected=tmp
        self.show_alert_dialog(f"Máximo {self.menu_mediodia_limit} menús","pizzas_roscas")
        return
    self.menu_mediodia_selected=tmp

@rx.event
def update_menu_mediodia_note(self, menu_type: str, value: str):
    tmp=dict(self.menu_mediodia_notes); tmp[menu_type]=value or ""
    self.menu_mediodia_notes=tmp
```

- [ ] Step 2: Actualizar select_pack para resetear menú y notas, y can_send/missing

```python
def select_pack(...):
    ...
    self.menu_mediodia_selected={t:0 for t in MENU_MEDIODOIA_TYPES}
    self.menu_mediodia_notes={t:"" for t in MENU_MEDIODOIA_TYPES}
```

```python
@rx.var
def can_send(self)->bool:
    base=bool(self.child_name.strip() and self.child_age.strip() and self.birth_date.strip() and self.birth_time.strip() and self.reservation_code.strip() and self.selected_bakery_option.strip())
    if not base: return False
    if self.cumple_tipo=="Cumple Mediodía":
        return self.menu_mediodia_total==self.menu_mediodia_limit
    return bool(self.selected_food_option.strip()) and self.total_pizza_rosca==self.max_allowed_pizza_rosca and self.total_drinks==self.max_allowed_drinks

@rx.var
def total_missing(self)->int:
    if self.cumple_tipo=="Cumple Mediodía":
        return max(0, self.menu_mediodia_limit - self.menu_mediodia_total)
    return self.missing_pizza_rosca+self.missing_drinks
```

- [ ] Step 3: collected_data incluir nuevas keys + compat alias

```python
"cumple_tipo": self.cumple_tipo,
"turno": "Mediodía" if self.cumple_tipo=="Cumple Mediodía" else "Tarde",
"tipo_cumple": "Mediodía" if self.cumple_tipo=="Cumple Mediodía" else "Tarde",
"menu_mediodia_selected": self.menu_mediodia_selected,
"menu_mediodia_notes": self.menu_mediodia_notes,
```

- [ ] Step 4: _generate_whatsapp_message y _save_order_to_supabase incluir sección MENÚ MEDIODÍA con notas, y payload detalle con todos los alias. Verificar py_compile.

---

### Task 3: pack_form.py - UI condicional

**Files:**
- Modify: `mena_cumples/components/pack_form.py:1-520`

- [ ] Step 1: Helpers _menu_mediodia_row y _menu_mediodia_section

```python
def _menu_mediodia_row(menu_type:str)->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.input(value=FormBaseState.menu_mediodia_selected[menu_type].to_string(), on_change=lambda v: FormBaseState.update_menu_mediodia(menu_type,v), width="60px", type="number"),
            rx.text(menu_type, weight="bold", color=Color.PURPLE_DARK),
            rx.spacer(),
            rx.badge(f"{FormBaseState.menu_mediodia_total}/{FormBaseState.menu_mediodia_limit}", color_scheme="amber"),
            width="100%", align_items="center"
        ),
        rx.input(placeholder="Ej: Sin lechuga, sin tomate / solo carne", value=FormBaseState.menu_mediodia_notes[menu_type], on_change=lambda v: FormBaseState.update_menu_mediodia_note(menu_type,v), width="100%", background_color=Color.WHITE),
        spacing="1", width="100%", padding="0.5rem", border="1px solid #fcd34d", border_radius="0.5rem", background_color="#fffbeb", margin_bottom="0.5rem"
    )
def _menu_mediodia_section()->rx.Component:
    return rx.vstack(
        rx.text("Menú Mediodía (cada uno incluye patatas + 1 bebida)", weight="bold", color="#92400e"),
        rx.text(f"Quedan {FormBaseState.menu_mediodia_remaining} de {FormBaseState.menu_mediodia_limit}", size="2", color="#b45309"),
        *[_menu_mediodia_row(t) for t in FormBaseState.MENU_MEDIODOIA_TYPES],
        width="100%", spacing="2"
    )
```

- [ ] Step 2: datos_personales usar FormBaseState.birth_times_options

```python
rx.select(FormBaseState.birth_times_options, value=FormBaseState.birth_time, on_change=FormBaseState.set_birth_time, placeholder="Hora")
```

- [ ] Step 3: Añadir selector Cumple tipo y condicional en pack_form

```python
_section_card("Tipo de cumple", rx.select(CUMPLE_TIPO_OPTIONS, value=FormBaseState.cumple_tipo, on_change=FormBaseState.set_cumple_tipo), icon_tag="calendar")
rx.cond(FormBaseState.cumple_tipo=="Cumple Mediodía",
    _section_card("Menú Mediodía", _menu_mediodia_section(), icon_tag="utensils", bg_color="#fffbeb"),
    rx.fragment(
        _section_card("Comida", seleccion_alimentos(...)),
        _section_card("Pizzas y Roscas", seleccion_pizzas(...)),
        _section_card("Bebidas", seleccion_bebidas(...)),
    )
)
# Extras y Repostería siempre visibles
```

- [ ] Step 4: Actualizar _missing_notice para mediodía
- [ ] Step 5: py_compile check `python -m py_compile mena_cumples/components/pack_form.py`

---

### Task 4: Sincronizar hotel_mena_plaza_web

**Files:**
- Modify: `hotel_mena_web/state/cumples_state.py:105`, `hotel_mena_web/components/email_templates.py:859`

- [ ] Cambiar BIRTH_TIMES_MEDIODOIA a ["13:00","13:30","14:00","14:30","15:00"] y ampliar _to_pedido para aceptar "cumple mediodía"/"cumple tarde" (contains mediodia)
- [ ] Actualizar CUMPLE_INFO_WHATSAPP_TEMPLATE: ya no decir "no disponible en web", sino "Disponible en web: Cumple Mediodía 13:00-15:00 y Tarde 16:00-19:00"
- [ ] Run `python -m py_compile hotel_mena_web/state/cumples_state.py` + `./.venv/bin/pytest tests/test_cumples_state.py -q` (esperado 36+ ok)

---

### Task 5: Verificación

- [ ] `python -m py_compile mena_cumples/states/form_state.py mena_cumples/components/pack_form.py`
- [ ] Manual: probar Pack_15 Cumple Mediodía -> seleccionar 8+7 menús + notas "sin lechuga", verificar can_send true solo si total==15, mensaje WhatsApp incluye MENÚ MEDIODÍA con notas, extras y repostería persisten.
- [ ] Probar Cumple Tarde sin regresión (pizzas+drinks).
