import json
import os

# Cargar datos del JSON maestro
with open(os.path.expanduser("~/fontaneria-netlify-ready/json_maestro/maestro.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

# Función para limpiar HTML de color y quedarnos solo con precio y medidas
def limpiar_capacidad(cap):
    partes = cap.split(",")
    precio = partes[0].split(":")[-1].replace('<span style="color:#FFA500">', '').replace('</span>', '').strip()
    medidas = partes[1].strip() if len(partes) > 1 else ""
    detalles = ", ".join(partes[2:]).strip() if len(partes) > 2 else ""
    return precio, medidas, detalles

# Generar HTML
html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Portada Termos</title>
<style>
body { font-family: Arial, sans-serif; margin: 20px; text-align: center; }
img { max-width: 100%; height: auto; object-fit: contain; }
.catalogo { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-top: 20px; }
.termo { border: 1px solid #ccc; padding: 10px; width: 250px; }
.boton { margin-top: 10px; padding: 10px 15px; background-color: #007BFF; color: white; text-decoration: none; display: inline-block; border-radius: 5px; }
</style>
</head>
<body>

<h1>SIMAT 195 litros</h1>
<img src="fontaneria-fotos/galeria/img/termos/SIMAT.jpg" alt="SIMAT 195L">
<br>
<a href="#catalogo" class="boton">Catálogo de termos, pincha aquí</a>

<div id="catalogo" class="catalogo">
"""

for termo in data:
    html += f'<div class="termo">'
    html += f'<h2>{termo["modelo"]}</h2>'
    html += f'<img src="fontaneria-fotos/galeria/img/termos/{termo["imagen"]}" alt="{termo["modelo"]}">'
    for cap in termo.get("capacidades", []):
        precio, medidas, detalles = limpiar_capacidad(cap)
        html += f'<p>{cap.split(":")[0]}: {precio}, {medidas}, {detalles}</p>'
    html += f'<p>{termo.get("descripcion", "")}</p>'
    html += f'<a class="boton" href="{termo["botones"]["whatsapp"]}" target="_blank">WhatsApp</a> '
    html += f'<a class="boton" href="tel:{termo["botones"]["llamar"]}">Llamar</a>'
    html += "</div>"

# Espacio para Fontanero Virtual
html += """
<div id="fontanero_virtual" style="margin-top:50px;">
<h2>Consulta Fontanero Virtual</h2>
<p>Escribe tu consulta y el motor te responderá.</p>
<!-- Aquí se integra el motor que ya tienes -->
</div>
"""

html += "</body></html>"

# Guardar archivo HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Catálogo y HTML final generados correctamente con todas las capacidades y fotos")
