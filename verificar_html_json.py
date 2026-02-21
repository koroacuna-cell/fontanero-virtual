import json
import os

JSON_PATH = os.path.expanduser("~/fontaneria-netlify-ready/json_maestro/maestro.json")
FOTOS_DIR = os.path.expanduser("~/Fontanero_Virtual_v4/fontaneria-fotos/galeria/img/termos")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    catalogo = json.load(f)

fotos_faltantes = []
datos_faltantes = []

for item in catalogo:
    # Verifica foto
    foto_path = os.path.join(FOTOS_DIR, item.get("imagen", ""))
    if not os.path.isfile(foto_path):
        fotos_faltantes.append(item.get("imagen", ""))
    
    # Verifica datos básicos
    if not item.get("modelo") or not item.get("capacidades") or not item.get("descripcion"):
        datos_faltantes.append(item.get("modelo", "SIN MODELO"))

if fotos_faltantes:
    print("❌ FOTOS FALTANTES:")
    for f in fotos_faltantes:
        print(" -", f)
else:
    print("✅ Todas las fotos existen y están en la carpeta correcta.")

if datos_faltantes:
    print("\n❌ DATOS INCOMPLETOS:")
    for d in datos_faltantes:
        print(" -", d)
else:
    print("✅ Todos los datos del JSON están completos y listos.")
