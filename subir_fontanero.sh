#!/bin/bash

# Configuración de usuario
git config --global user.name "Eduardo Quiróz"
git config --global user.email "koroacuna@gmail.com"

# Entrar al directorio del proyecto
cd ~/Fontanero_Virtual_v4 || { echo "No se encuentra el directorio"; exit 1; }

# Inicializar repositorio (si no está inicializado)
git init

# Añadir archivo
git add fontanero_virtual_completo.html

# Commit
git commit -m "Subida inicial del Fontanero Virtual"

# Configurar remoto (sobrescribir si ya existe)
git remote set-url origin https://github.com/TU_USUARIO/fontanero-virtual.git

# Push al repositorio usando token
# IMPORTANTE: Cambia TU_TOKEN por tu token de GitHub
echo "Introduce tu token de GitHub como contraseña cuando se te pida"
git push -u origin main
