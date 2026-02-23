document.addEventListener('DOMContentLoaded', () => {
    const messages = document.getElementById('messages');
    const input = document.getElementById('input');
    const enviarBtn = document.getElementById('send-btn');

    function logConsola(mensaje){
        console.log('[Fontanero Debug]', mensaje);
    }

    function agregarMensajeBot(texto){
        const div = document.createElement('div');
        div.classList.add('bot');
        div.innerHTML = texto;
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
    }

    function agregarMensajeUsuario(texto){
        const div = document.createElement('div');
        div.classList.add('user');
        div.textContent = texto;
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
    }

    // Inicialización de motores
    function inicializarMotor(nombre){
        messages.innerHTML = '';
        try {
            if(nombre === 'V4' && window.MotorV4){
                window.motorFontanero = new window.MotorV4('/catalogo_termos.json');
                logConsola('Motor V4 cargado correctamente.');
                agregarMensajeBot('Motor V4 listo.');
            } else if(nombre === 'V3' && window.MotorV3){
                window.motorFontanero = new window.MotorV3('/catalogo_termos.json');
                logConsola('Motor V3 cargado correctamente.');
                agregarMensajeBot('Motor V3 listo.');
            } else if(nombre === 'Vendedor' && window.MotorVendedor){
                window.motorFontanero = new window.MotorVendedor('/maestro_vendedor.json');
                logConsola('Motor Vendedor cargado correctamente.');
                agregarMensajeBot('Motor Vendedor listo.');
            } else {
                window.motorFontanero = null;
                logConsola('Motor no disponible o no definido.');
                agregarMensajeBot('Motor no disponible.');
            }
        } catch(err){
            window.motorFontanero = null;
            logConsola('Error al cargar el motor: ' + err);
            agregarMensajeBot('Error al cargar el motor. Revisa la consola.');
        }
    }

    enviarBtn.addEventListener('click', () => {
        const texto = input.value.trim();
        if(!texto) return;
        agregarMensajeUsuario(texto);
        input.value = '';

        if(window.motorFontanero){
            const lang = texto.toLowerCase().includes('english') ? 'en' : 'es';
            const respuesta = window.motorFontanero.procesarConsulta(texto, lang);
            if(respuesta){
                agregarMensajeBot(respuesta);
            } else {
                agregarMensajeBot(lang === 'es' ? 'No he entendido la consulta. Envíame una foto por WhatsApp.' : 'I did not understand your query. Send a photo via WhatsApp.');
            }
        } else {
            agregarMensajeBot('Motor no cargado correctamente.');
        }
    });

    input.addEventListener('keypress', (e) => {
        if(e.key === 'Enter'){
            e.preventDefault();
            enviarBtn.click();
        }
    });

    // Inicializar motor por defecto
    if(window.MotorV4){
        inicializarMotor('V4');
    } else if(window.MotorV3){
        inicializarMotor('V3');
    } else if(window.MotorVendedor){
        inicializarMotor('Vendedor');
    }
});
