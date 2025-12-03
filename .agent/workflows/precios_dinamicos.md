---
description: Sistema de precios dinámicos por año
---

# Sistema de Precios Dinámicos

## Descripción

El sistema ahora calcula automáticamente el precio de los packs según el año de la fecha del cumpleaños seleccionada.

## Funcionamiento

### Precios Base (2025)

- Pack 15 personas: 90€
- Pack 20 personas: 120€
- Pack 25 personas: 150€
- Pack 30 personas: 180€

### Incremento para 2026 y posteriores

- Todos los packs tienen un incremento de **20€** para fechas en 2026 o años posteriores

### Precios 2026

- Pack 15 personas: 110€
- Pack 20 personas: 140€
- Pack 25 personas: 170€
- Pack 30 personas: 200€

## Implementación Técnica

### Archivos modificados:

1. **`mena_cumples/states/form_state.py`**

   - Añadido `PACK_BASE_PRICES`: diccionario con precios base
   - Añadido `PRICE_INCREASE_2026`: constante con el incremento (20€)
   - Método `get_pack_price()`: calcula el precio según el año de `birth_date`
   - Método `pack_title_with_price()`: genera el título del pack con precio dinámico
   - Modificado `send_whatsapp_message()`: usa el precio dinámico

2. **`mena_cumples/components/pack_form.py`**

   - El heading del pack ahora usa `FormBaseState.pack_title_with_price`
   - El precio se actualiza automáticamente cuando el usuario cambia la fecha

3. **`mena_cumples/pages/pack_selection_page.py`**

   - Añadido callout informativo sobre el incremento de precios para 2026
   - Función `_create_pack_card()` actualizada para mostrar ambos precios
   - Cada tarjeta muestra: precio 2025, precio 2026 y badge "+20€"
   - `PACK_OPTIONS_DATA` incluye campos `price_2025`, `price_2026`, `num_people`

4. **`mena_cumples/pages/packs_information_page.py`**
   - Añadido callout informativo al inicio de la página
   - Cada pack muestra ambos precios (2025 y 2026) con badge "+20€"
   - Formato: "2025: 90€ • 2026: 110€ [+20€]"
   - Diseño mejorado con colores diferenciados para cada año

## Comportamiento

1. **Página de selección**: Muestra precios base (2025) con nota informativa
2. **Formulario del pack**:
   - Al cargar, muestra precio base
   - Cuando el usuario selecciona una fecha en 2026 o posterior, el precio se actualiza automáticamente a +20€
3. **Mensaje de WhatsApp**: Incluye el precio correcto según la fecha seleccionada

## Modificar precios en el futuro

Para cambiar los precios base o el incremento, edita en `form_state.py`:

```python
# Precios base (año 2025)
PACK_BASE_PRICES = {
    "Pack_15": 90,
    "Pack_20": 120,
    "Pack_25": 150,
    "Pack_30": 180,
}

# Incremento de precio para 2026 en adelante
PRICE_INCREASE_2026 = 20
```

Para añadir precios para 2027, modifica el método `get_pack_price()`.
