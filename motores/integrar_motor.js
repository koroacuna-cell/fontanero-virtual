document.addEventListener('DOMContentLoaded', () => {

    const container = document.getElementById('fontanero-virtual-container');

    container.innerHTML = `
        <div id="messages" style="height:300px;overflow-y:auto;border:1px solid #ccc;padding:10px;margin-bottom:10px;"></div>
        <div id="input-container">
            <input id="input" placeholder="Describe tu problema..." />
            <button id="enviar-btn">Enviar</button>
        </div>
    `;

    const input = document.getElementById('input');
    const enviarBtn = document.getElementById('enviar-btn');
    const messages = document.getElementById('messages');

    function agregarMensajeUsuario(texto){
        const div = document.createElement('div');
        div.textContent = texto;
        div.style.textAlign = 'right';
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
    }

    function agregarMensajeBot(texto){
        const div = document.createElement('div');
        div.innerHTML = texto;
        div.style.textAlign = 'left';
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
    }

    enviarBtn.addEventListener('click', () => {
        const texto = input.value.trim();
        if(!texto) return;

        agregarMensajeUsuario(texto);
        input.value = '';

        if(window.motorFontanero){
            const procesado = window.motorFontanero.procesarConsulta(texto);
            if(!procesado){
                agregarMensajeBot('No he entendido la consulta. Envíame una foto por WhatsApp.');
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

});
