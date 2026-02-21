import json
import os
import shutil

# JSON maestro
json_path = '/data/data/com.termux/files/home/fontaneria-netlify-ready/json_maestro/maestro.json'

# Carpeta destino limpia
destino = '/data/data/com.termux/files/home/Fontanero_Virtual_v4/fontaneria-fotos/galeria/img/termos'
os.makedirs(destino, exist_ok=True)

# Carpeta(s) donde buscar fotos (puedes agregar más)
fuentes = [
    '/data/data/com.termux/files/home/backup_20251125_temp',
    '/data/data/com.termux/files/home/restore_backup',
    '/data/data/com.termux/files/home/FontaneroLimpio',
    '/data/data/com.termux/files/home/FontaneroLimpio_trabajo',
    '/data/data/com.termux/files/home/FontaneroProyecto/restaurado/FontaneroLimpio_restaure',
    '/data/data/com.termux/files/home/export_fontanero/FontaneroLimpio'
]

# Leer JSON
with open(json_path, 'r', encoding='utf-8') as f:
    catalogo = json.load(f)

faltantes = []

for producto in catalogo:
    foto = producto['imagen']
    encontrada = False
    for src_base in fuentes:
        for root, _, files in os.walk(src_base):
            if foto in files:
                src_path = os.path.join(root, foto)
                dest_path = os.path.join(destino, foto)
                shutil.copy2(src_path, dest_path)
                print(f"✅ Copiada {foto} desde {src_path}")
                encontrada = True
                break
        if encontrada:
            break
    if not encontrada:
        print(f"❌ FALTA {foto}")
        faltantes.append(foto)

print("\n=== RESUMEN ===")
if faltantes:
    print("Fotos faltantes:")
    for f in faltantes:
        print(f" - {f}")
else:
    print("Todas las fotos están presentes y copiadas correctamente.")
