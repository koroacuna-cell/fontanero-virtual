import os
import json
import shutil

# Ruta del JSON maestro
json_path = os.path.expanduser('~/fontaneria-netlify-ready/json_maestro/maestro.json')

# Carpeta limpia de destino para las fotos
dest_folder = os.path.expanduser('~/Fontanero_Virtual_v4/fontaneria-fotos/galeria/img/termos')
os.makedirs(dest_folder, exist_ok=True)

# Carpetas donde buscar las fotos
search_dirs = [
    os.path.expanduser('~/Fontanero_Virtual_v3/fontaneria-fotos'),
    os.path.expanduser('~/Fontanero_Virtual_v4/fontaneria-fotos'),
    os.path.expanduser('~/fontaneria-netlify-ready')
]

# Cargar JSON maestro
with open(json_path, 'r', encoding='utf-8') as f:
    productos = json.load(f)

faltantes = []

# Función para buscar archivo en directorios
def buscar_archivo(nombre):
    for d in search_dirs:
        for root, _, files in os.walk(d):
            if nombre in files:
                return os.path.join(root, nombre)
    return None

# Procesar cada producto
for p in productos:
    img_name = p['imagen']
    origen = buscar_archivo(img_name)
    if origen:
        destino = os.path.join(dest_folder, img_name)
        if os.path.abspath(origen) != os.path.abspath(destino):
            shutil.copy2(origen, destino)
            print(f"✅ Copiado {img_name}")
        else:
            print(f"⚠️ Ya estaba en destino: {img_name}")
        p['foto'] = os.path.relpath(destino, os.path.expanduser('~/Fontanero_Virtual_v4'))
    else:
        faltantes.append(img_name)
        print(f"❌ FALTA {img_name}")

# Guardar JSON limpio
json_limpio_path = os.path.expanduser('~/Fontanero_Virtual_v4/catalogo_termos.json')
with open(json_limpio_path, 'w', encoding='utf-8') as f:
    json.dump(productos, f, ensure_ascii=False, indent=4)

print("\n=== RESUMEN ===")
if faltantes:
    print("Fotos faltantes:")
    for f in faltantes:
        print(f" - {f}")
else:
    print("Todas las fotos copiadas correctamente.")
