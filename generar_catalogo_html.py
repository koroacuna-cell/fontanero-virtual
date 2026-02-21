import json
import os

# Rutas
json_file = "maestro.json"
output_file = "index.html"
img_path = "fontaneria-fotos/galeria/img/termos/"

# Leer JSON maestro
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Generar HTML
html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Catálogo de Termos - Fontanería Eduardo Quirós</title>
<style>
body { font-family: Arial, sans-serif; margin: 20px; background: #f7f7f7; }
h1 { text-align: center; }
.catalogo { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
.termo { background: white; padding: 10px; border-radius: 8px; width: 250px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
.termo img { width: 200px; height: 200px; object-fit: contain; margin-bottom: 10px; }
.precio { color: #FFA500; font-weight: bold; }
</style>
</head>
<body>
<h1>Catálogo de Termos - Fontanería Eduardo Quirós</h1>
<div class="catalogo">
"""

# Iterar sobre todos los modelos
for termo in data:
    # Foto base de 50L
    foto = termo.get("foto", "")
    html += f'<div class="termo">\n'
    html += f'<img src="{img_path}{foto}" alt="{termo["modelo"]}">\n'
    html += f'<h2>{termo["modelo"]}</h2>\n'
    
    # Iterar sobre capacidades disponibles
    for cap in termo.get("capacidades", []):
        litros = cap.get("litros", "")
        precio = cap.get("precio", "")
        medidas = cap.get("medidas", "")
        html += f'<p>Litros: {litros} L</p>\n'
        html += f'<p>Medidas: {medidas}</p>\n'
        html += f'<p class="precio">Precio: {precio}€</p>\n'
    
    html += '</div>\n'

html += """
</div>
</body>
</html>
"""

# Guardar HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Catálogo y HTML actualizados correctamente con todas las capacidades y fotos")
