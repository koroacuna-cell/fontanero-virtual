import json
import os
import shutil

# Rutas
json_maestro = "/data/data/com.termux/files/home/fontaneria-netlify-ready/json_maestro/maestro.json"
fotos_origen = "/data/data/com.termux/files/home/Fontanero_Virtual_v3/fontaneria-fotos/galeria/img/termos"
proyecto_limpio = "/data/data/com.termux/files/home/Fontanero_Virtual_v4"
fotos_destino = os.path.join(proyecto_limpio, "fontaneria-fotos/galeria/img/termos")

# Crear estructura limpia
os.makedirs(fotos_destino, exist_ok=True)
os.makedirs(os.path.join(proyecto_limpio, "motores"), exist_ok=True)

# Leer JSON maestro
with open(json_maestro, "r", encoding="utf-8") as f:
    catalogo = json.load(f)

# Lista de problemas
faltantes = []

# Copiar fotos existentes y detectar faltantes
for item in catalogo:
    foto_nombre = item["imagen"]
    origen = os.path.join(fotos_origen, foto_nombre)
    destino = os.path.join(fotos_destino, foto_nombre)
    if os.path.isfile(origen):
        shutil.copy2(origen, destino)
    else:
        faltantes.append(foto_nombre)

# Guardar JSON maestro limpio en la carpeta nueva
json_destino = os.path.join(proyecto_limpio, "maestro.json")
with open(json_destino, "w", encoding="utf-8") as f:
    json.dump(catalogo, f, ensure_ascii=False, indent=2)

# Resultados
if faltantes:
    print("=== FOTOS FALTANTES ===")
    for f in faltantes:
        print(f"- {f}")
else:
    print("✅ Todas las fotos están presentes y copiadas correctamente.")
