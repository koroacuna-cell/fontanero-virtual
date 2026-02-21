import json
import os

JSON_PATH = "catalogo_termos.json"
BASE_FOTOS = "fontaneria-fotos/galeria/img/termos"

# Cargar JSON
try:
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        catalogo = json.load(f)
except Exception as e:
    print(f"❌ Error cargando JSON: {e}")
    exit(1)

errores = []

for p in catalogo:
    nombre = p.get("nombre", "")
    litros = p.get("litros", "")
    foto = p.get("foto", "")

    if not nombre or not litros:
        errores.append(f"❌ Datos incompletos: {nombre} - {litros}")
    
    if not os.path.isfile(foto):
        errores.append(f"❌ Foto no encontrada para {nombre}: {foto}")

if errores:
    print("=== PROBLEMAS EN EL CATÁLOGO ===")
    for e in errores:
        print("-", e)
    print("=== FIN DE LA VERIFICACIÓN ===")
else:
    print("✅ Todo correcto, JSON y fotos presentes.")
