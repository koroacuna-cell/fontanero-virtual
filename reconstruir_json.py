import json
import os

# Ruta del JSON maestro original
json_maestro = '/data/data/com.termux/files/home/fontaneria-netlify-ready/json_maestro/maestro.json'

# Carpeta donde están las fotos reales de la copia maestro
carpeta_fotos = '/data/data/com.termux/files/home/CopiaMaestroFotos'

# Ruta de salida del JSON limpio
json_salida = '/data/data/com.termux/files/home/Fontanero_Virtual_v4/catalogo_termos_limpio.json'

# Listar todas las fotos disponibles
fotos_disponibles = {os.path.basename(f): f for f in os.listdir(carpeta_fotos) if f.lower().endswith(('.jpg', '.png'))}

# Leer JSON maestro
with open(json_maestro, 'r', encoding='utf-8') as f:
    catalogo = json.load(f)

# Reconstruir JSON con rutas correctas
nuevo_catalogo = []
faltantes = []

for item in catalogo:
    img = item['imagen']
    if img in fotos_disponibles:
        item['foto'] = fotos_disponibles[img]  # ruta completa desde la copia maestro
        nuevo_catalogo.append(item)
    else:
        faltantes.append(img)

# Guardar JSON limpio
with open(json_salida, 'w', encoding='utf-8') as f:
    json.dump(nuevo_catalogo, f, ensure_ascii=False, indent=2)

# Resumen
if faltantes:
    print("=== FOTOS FALTANTES ===")
    for f in faltantes:
        print("-", f)
else:
    print("✅ Todas las fotos localizadas y JSON limpio generado correctamente.")
