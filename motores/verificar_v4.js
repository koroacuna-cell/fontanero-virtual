// Motor JS para Fontanero Virtual Eduardo Quiroz
// Filtra termos por litros y muestra descripción, precio, instalación e idioma

const idioma = 'es'; // Cambiar a 'en' para inglés

// Cargar catálogo de termos desde JSON
fetch('recomendaciones_completa.json')
  .then(response => response.json())
  .then(data => {
    window.catalogoTermos = data;
  })
  .catch(err => console.error('Error cargando JSON:', err));

function buscarTermo(litros) {
    const resultados = [];
    for (const modelo in window.catalogoTermos) {
        const termo = window.catalogoTermos[modelo];
        termo.capacidades.forEach(c => {
            if (c.litros === litros) {
                resultados.push({
                    nombre: modelo,
                    litros: c.litros,
                    precio: c.precio,
                    descripcion: idioma === 'es' ? termo.descripcion_es : termo.descripcion_en
                });
            }
        });
    }
    return resultados;
}

function mostrarResultados(litros) {
    const container = document.getElementById('messages');
    container.innerHTML = '';
    const resultados = buscarTermo(litros);
    if(resultados.length === 0){
        container.innerHTML = idioma === 'es' ? 'No hay termos de esa capacidad' : 'No water heaters with this capacity';
        return;
    }
    resultados.forEach(r => {
        const div = document.createElement('div');
        div.classList.add('bot');
        div.innerHTML = `<strong>${r.nombre}</strong><br>
                         ${r.litros}L - ${r.precio}€<br>
                         ${r.descripcion}`;
        container.appendChild(div);
    });
}

// Función para usar en el input del chat
function procesarConsulta(texto) {
    texto = texto.toLowerCase();
    const litrosMatch = texto.match(/(\d+)\s*litros?/i);
    if(litrosMatch){
        const litros = parseInt(litrosMatch[1],10);
        mostrarResultados(litros);
        return true;
    }
    return false;
}

// Export para integrarlo con tu sistema de chat
window.motorFontanero = {
    procesarConsulta
};
