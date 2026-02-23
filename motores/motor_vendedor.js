// Motor JS para Fontanero Virtual - maestro_vendedor.json
// Lee el JSON de termos y genera respuestas filtradas por litros

async function cargarTermos() {
    const response = await fetch('maestro_vendedor.json');
    const data = await response.json();
    return data.termos;
}

// Función para generar respuesta de chat
async function responderConsulta(consulta) {
    const termos = await cargarTermos();
    consulta = consulta.toLowerCase();

    // Respuestas por defecto
    const defaultMsg = {
        es: "No he entendido bien la consulta. Envíame una foto por WhatsApp y te ayudo inmediatamente.",
        en: "I didn't understand the query. Send me a photo via WhatsApp and I will help you immediately."
    };

    // Comprobar palabras clave
    if (consulta.includes('fuga') || consulta.includes('pierde agua')) {
        return {
            es: "Las fugas pueden deberse a juntas deterioradas o presión excesiva. Envíame una foto por WhatsApp y te ayudo inmediatamente.",
            en: "Leaks can be due to worn gaskets or excessive pressure. Send me a photo via WhatsApp and I will help you immediately."
        };
    }

    if (consulta.includes('termo')) {
        // Buscar si mencionan litros
        const litrosMatch = consulta.match(/\b(\d{2,3})\s?l/);
        let litrosFiltro = litrosMatch ? parseInt(litrosMatch[1]) : null;

        let catalogo = termos.map(t => {
            let capacidades = t.capacidades;
            if (litrosFiltro) {
                capacidades = capacidades.filter(c => c.litros === litrosFiltro);
            }
            if (capacidades.length === 0) return null;
            let detalles = capacidades.map(c => `- ${c.litros}L: ${c.precio}€`).join('\n');
            return {
                nombre: t.nombre,
                descripcion_es: `${t.descripcion_es}\n${detalles}\nInstalación incluida, más IVA.\nFicha: ${t.link}`,
                descripcion_en: `${t.descripcion_en}\n${detalles}\nInstallation included, plus VAT.\nLink: ${t.link}`
            };
        }).filter(x => x !== null);

        if (catalogo.length === 0) return {
            es: "No hay termos disponibles con esa capacidad.",
            en: "No water heaters available with that capacity."
        };

        // Generar mensaje concatenado
        let msg_es = catalogo.map(c => `${c.nombre}\n${c.descripcion_es}`).join('\n\n');
        let msg_en = catalogo.map(c => `${c.nombre}\n${c.descripcion_en}`).join('\n\n');

        return { es: msg_es, en: msg_en };
    }

    return defaultMsg;
}

// Exportar función para uso en index.html
window.responderConsulta = responderConsulta;
