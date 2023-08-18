document.addEventListener("DOMContentLoaded", () => {
    const chatContainer = document.getElementById("chat-container");
    const userMessageInput = document.getElementById("user-message");
    const sendButton = document.getElementById("send-button");
    const chat = document.querySelector(".chat");

    sendButton.addEventListener("click", () => {
        console.log('oojsodjfosdjfosdfd');
        debugger;
        const userMessage = userMessageInput.value;
        if (userMessage.trim() !== "") {
            appendMessage(userMessage, "user");
            sendMessageToServer(userMessage);
            userMessageInput.value = "";
        }
    });

    const menuButtons = document.querySelectorAll(".menu-button");
    menuButtons.forEach(button => {
        button.addEventListener("click", () => {
            const option = button.getAttribute("data-option");
            appendMessage(option, "user");
            executeOptionLogic(option);
        });
    });

    function appendMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.textContent = message;
        chat.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function handleBotResponse(response) {
        if (response === "choose_category") {
            showCategoryOptions();
        } else {
            appendMessage(response, "bot");
        }
    }

    function sendMessageToServer(message) {
        $.ajax({
            url: "/chatbot_response/",
            data: { user_message: message },
            dataType: "json",
            success: function (response) {
                handleBotResponse(response.response);
            },
            error: function () {
                handleBotResponse("Вибачте, сталася помилка.");
            }
        });
    }
    function executeOptionLogic(option) {
        $.ajax({
            url: "/execute_option_logic/",
            data: { selected_option: option },
            dataType: "json",
            success: function (response) {
                handleBotResponse(response.response);
            },
            error: function () {
                handleBotResponse("Вибачте, сталася помилка.");
            }
        });
    }
    function showCategoryOptions() {
        const optionsDiv = document.createElement("div");
        optionsDiv.classList.add("options");

        const categories = ["Електроніка", "Одяг", "Косметика"];
        categories.forEach(category => {
            const button = document.createElement("button");
            button.classList.add("menu-button");
            button.textContent = category;
            button.setAttribute("data-option", category);
            optionsDiv.appendChild(button);
        });

        chat.appendChild(optionsDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});