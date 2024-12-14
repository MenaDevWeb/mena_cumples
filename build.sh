#!/bin/bash

# Activar el entorno virtual
source .venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar las dependencias
pip install -r requirements.txt

# Inicializar Reflex
reflex init

# Exportar el backend y frontend
reflex export --frontend-only

# Eliminar el directorio `public` existente
rm -rf public

# Descomprimir el frontend
unzip frontend.zip -d public

# Eliminar el archivo `frontend.zip`
rm -f frontend.zip

# Desactivar el entorno virtual
deactivate