import os
from PIL import Image, ImageDraw, ImageFont

# Carpeta destino
dest = os.path.expanduser('~/Fontanero_Virtual_v4/fontaneria-fotos/galeria/img/termos')
os.makedirs(dest, exist_ok=True)

# Lista de fotos faltantes
faltantes = ["MULTIDRIVE.jpg", "HIBRIDO-WIFI.jpg", "NUOS-EVO.jpg"]

for f in faltantes:
    ruta = os.path.join(dest, f)
    # Crear imagen 300x300 gris
    img = Image.new('RGB', (300, 300), color='gray')
    draw = ImageDraw.Draw(img)
    texto = f
    # Fuente por defecto
    draw.text((10, 140), texto, fill='black')
    img.save(ruta)
    print(f"✅ Placeholder creado: {ruta}")
