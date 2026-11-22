const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");

function addMessage(message, className, label) {
    const messageElement = document.createElement("div");
    messageElement.className = `message ${className}`;

    if (label) {
        const heading = document.createElement("strong");
        heading.textContent = label;
        messageElement.appendChild(heading);
    }

    const paragraph = document.createElement("p");
    paragraph.textContent = message;
    messageElement.appendChild(paragraph);

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user-message", "You");
    userInput.value = "";
    sendButton.disabled = true;
    sendButton.textContent = "Sending...";

    try {
        // This relative URL works when the page is served by the Flask app.
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.response || `HTTP ${response.status}`);
        }

        addMessage(data.response, "bot-message", "Assistant");
    } catch (error) {
        console.error("Chat request failed:", error);
        addMessage(
            "Could not reach the chatbot server. Make sure Flask is running and open this page at http://127.0.0.1:5000.",
            "error-message",
            "Connection problem"
        );
    } finally {
        sendButton.disabled = false;
        sendButton.textContent = "Send";
        userInput.focus();
    }
});
