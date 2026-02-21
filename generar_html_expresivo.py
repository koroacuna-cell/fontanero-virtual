import json
import os

json_path = os.path.expanduser("~/fontaneria-netlify-ready/json_maestro/maestro.json")
output_html = os.path.expanduser("~/Fontanero_Virtual_v4/index.html")

with open(json_path, "r", encoding="utf-8") as f:
    termos = json.load(f)

html_head = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Catálogo Termos - Fontanero Virtual</title>
<style>
body { font-family: Arial, sans-serif; margin:0; padding:0; background:#f5f5f5; }
.container { display:flex; flex-wrap:wrap; justify-content:center; padding:20px; gap:20px; }
.card { background:#fff; width:300px; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1); padding:15px; }
.card img { width:100%; height:auto; border-radius:5px; }
.capacidad { display:flex; justify-content:space-between; font-weight:bold; margin:5px 0; }
.cap50 { color:#FFA500; }
.cap80 { color:#00BFFF; }
.cap100 { color:#32CD32; }
.boton { display:inline-block; padding:10px 15px; margin:5px 5px 0 0; background:#FF4500; color:#fff; text-decoration:none; border-radius:5px; font-weight:bold; }
.boton-catalogo { background:#1E90FF; }
.fontanero { text-align:center; margin:30px 0; padding:20px; background:#eee; border-radius:10px; }
</style>
</head>
<body>
<h1 style="text-align:center; padding:20px;">Catálogo Termos - Fontanero Virtual</h1>
<div class="container">
"""

html_body = ""
for termo in termos:
    img = termo.get("imagen", "")
    html_body += f'<div class="card">'
    html_body += f'<img src="fontaneria-fotos/galeria/img/termos/{img}" alt="{termo.get("modelo","")}">'
    html_body += f'<h2>{termo.get("modelo","")}</h2>'
    
    for cap in termo.get("capacidades", []):
        # Extraemos litros y precio + detalles sin #FFA500
        partes = cap.split(":")
        litros = partes[0].strip()
        detalles = ":".join(partes[1:]).replace('#FFA500">','').strip()
        color_class = "cap50" if "50" in litros else "cap80" if "80" in litros else "cap100"
        html_body += f'<div class="capacidad {color_class}"><span>{litros}</span><span>{detalles}</span></div>'
    
    html_body += f'<p>{termo.get("descripcion","")}</p>'
    html_body += f'<a class="boton" href="{termo.get("botones", {}).get("whatsapp","#")}">WhatsApp</a>'
    html_body += f'<a class="boton" href="tel:{termo.get("botones", {}).get("llamar","#")}">Llamar</a>'
    html_body += '</div>'

html_footer = """
</div>
<div class="fontanero">
<h2>Consulta Fontanero Virtual</h2>
<p>Escribe tu consulta y el motor te responderá.</p>
<!-- Aquí se integrarán los motores de consulta -->
</div>
</body>
</html>
"""

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_head + html_body + html_footer)

print("✅ HTML expresivo generado correctamente en index.html")
