// app/static/app.js
async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    const chatWindow = document.getElementById('chat-window');

    // Display user's message
    const userMessage = document.createElement('p');
    userMessage.classList.add('message', 'user-message');
    userMessage.innerHTML = `<strong>You:</strong> ${message}`;
    chatWindow.appendChild(userMessage);

    // Scroll to the bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Send the message to the backend API
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ question: message })
    });

    const data = await response.json();

    // Display bot's response
    const botMessage = document.createElement('p');
    botMessage.classList.add('message', 'bot-message');
    botMessage.innerHTML = `<strong>Bot:</strong> ${data.reply}`;
    chatWindow.appendChild(botMessage);

    // Scroll again after bot's reply
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Clear input field
    input.value = '';
}
