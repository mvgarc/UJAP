document.addEventListener('DOMContentLoaded', (event) => {
    // Escucha la tecla 'Enter' en el campo de entrada
    document.getElementById('input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            enviar();
        }
    });
});

function enviar() {
    const inputField = document.getElementById('input');
    const userMessage = inputField.value.trim();

    if (userMessage === "") {
        return; // No enviar si el mensaje está vacío
    }

    // 1. Mostrar el mensaje del usuario en el chat
    displayMessage(userMessage, 'user-message');

    // 2. Enviar el mensaje al backend de Flask
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        // Nota: Corregí el error tipográfico 'mensjase' a 'mensaje'
        body: JSON.stringify({ mensaje: userMessage }) 
    })
    .then(response => response.json())
    .then(data => {
        // 3. Mostrar la respuesta del bot
        displayMessage(data.respuesta, 'bot-message');
    })
    .catch(error => {
        console.error('Error al enviar el mensaje:', error);
        displayMessage("Error: No se pudo conectar con el servidor.", 'bot-message');
    });

    // 4. Limpiar el campo de entrada
    inputField.value = '';
}

function displayMessage(message, className) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    messageElement.textContent = message;
    
    messagesDiv.appendChild(messageElement);
    
    // Hacer scroll al final para ver el último mensaje
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}