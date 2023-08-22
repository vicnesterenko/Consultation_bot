const menu = document.querySelector(".menu");
const menuItems = document.querySelectorAll(".menuItem");
const hamburger = document.querySelector(".hamburger");
const closeIcon = document.querySelector(".closeIcon");
const menuIcon = document.querySelector(".menuIcon");

function toggleMenu() {
    if (menu.classList.contains("showMenu")) {
        menu.classList.remove("showMenu");
        closeIcon.style.display = "none";
        menuIcon.style.display = "block";
    } else {
        menu.classList.add("showMenu");
        closeIcon.style.display = "block";
        menuIcon.style.display = "none";
    }
}

hamburger.addEventListener("click", toggleMenu);

menuItems.forEach(
    function (menuItem) {
        menuItem.addEventListener("click", toggleMenu);
    }
)

/////////////////////////////////////////////////////
// paste all json here
// var data = JSON.parse('{{ data | safe }}');

function showUserChoise(text) {
    var contentBlock = document.querySelector('.modal-content');

    // Create a new chat message element
    var userAnswers = document.createElement("div");
    userAnswers.className = "user-answers";
    var answerSection = document.createElement("section");
    answerSection.className = "answer";
    var fromUserDiv = document.createElement("div");
    fromUserDiv.className = "from-user";
    var messageParagraph = document.createElement("p");
    messageParagraph.textContent = text; // Set the text to the button text
    fromUserDiv.appendChild(messageParagraph);
    answerSection.appendChild(fromUserDiv);
    userAnswers.appendChild(answerSection);

    contentBlock.appendChild(userAnswers);
}

function findNextInfo(data, next_id) {
    console.log(data)//TODO testing
    console.log(next_id)//TODO testing
    obj = data[next_id];
    return obj;
}

function createToDoButtons(obj) {
    var contentBlock = document.querySelector('.modal-content');

    var toDoButtonsDiv = document.createElement("div");
    toDoButtonsDiv.className = "to-do-buttons";

    var sreviewsSection = document.createElement("section");
    sreviewsSection.className = "sreviews";

    var fromBotDiv = document.createElement("div");
    fromBotDiv.className = "from-bot";

    var questionParagraph = document.createElement("p");
    questionParagraph.textContent = obj.q;

    fromBotDiv.appendChild(questionParagraph);
    sreviewsSection.appendChild(fromBotDiv);

    var buttonsDiv = document.createElement("div");
    buttonsDiv.className = "buttons";

    // Loop through the options and create buttons
    obj.options.forEach(function (option) {
        var button = document.createElement("button");
        button.id = option.next_id;
        button.className = "button";
        button.textContent = option.label;

        buttonsDiv.appendChild(button);
    });

    toDoButtonsDiv.appendChild(sreviewsSection);
    toDoButtonsDiv.appendChild(buttonsDiv);

    contentBlock.appendChild(toDoButtonsDiv);

}




function my_function() {
    const buttons = document.querySelectorAll(".button");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {

            showUserChoise(button.textContent);

            obj = findNextInfo(data, button.getAttribute("id"))
            console.log(obj) //TODO testing

            if (obj["type"] == "link") {
                console.log("It`s a link"); //TODO testing
                createLinks(obj);

            } else if (obj["type"] == "question") {
                console.log("It`s a question"); //TODO testing
                createToDoButtons(obj);

                my_function() // restart the function to add eventlistener for new buttons
            }
        });
    });
}

my_function()


