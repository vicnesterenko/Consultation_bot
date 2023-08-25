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

function createButtons(obj){
    var buttonsDiv = document.createElement("div");
    buttonsDiv.className = "buttons";
    // Loop through the options and create buttons
    obj.options.forEach(function (option) {
        var button = document.createElement("button");
        button.id = option.next_id;
        if (button.id == "manager"){
            button.classList.add("button-manager", "button");
            button.title = "Зв'язатись з менеджером";
        }else if (button.id == "back"){
            button.classList.add("button-prev", "button");
        }else{
            button.className = "button";
        }
        
        button.textContent = option.label;

        buttonsDiv.appendChild(button);
    });
    return buttonsDiv;
}

/**
function findNextInfo(data, next_id) {
    console.log(data)//TODO testing
    console.log(next_id)//TODO testing
    obj = data[next_id];
    return obj;
}
*/

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


    buttonsDiv = createButtons(obj);

    toDoButtonsDiv.appendChild(sreviewsSection);
    toDoButtonsDiv.appendChild(buttonsDiv);

    contentBlock.appendChild(toDoButtonsDiv);
}

function createLinks(obj) {
    var contentBlock = document.querySelector('.modal-content');

    var toDoButtonsDiv = document.createElement("div");
    toDoButtonsDiv.className = "to-do-buttons";

    var i = 0;
    obj.texts.forEach(function (text) {
        var linkElement = document.createElement("a");
        linkElement.setAttribute("class", "");
        linkElement.setAttribute("href", text["url"]);
        linkElement.textContent = `${i + 1}. ${text["name"]}`;
        const fromBotDiv = document.createElement("div");
        fromBotDiv.setAttribute("class", "from-bot");
        fromBotDiv.appendChild(linkElement);
        i = i + 1;
        toDoButtonsDiv.appendChild(fromBotDiv)
    });

    buttonsDiv = createButtons(obj);

    toDoButtonsDiv.appendChild(buttonsDiv);
    contentBlock.appendChild(toDoButtonsDiv);
}


function createQuestionLink(obj){
    var contentBlock = document.querySelector('.modal-content');

    var toDoButtonsDiv = document.createElement("div");
    toDoButtonsDiv.className = "to-do-buttons";

    // Create first message/messages
    obj.q.forEach(function (que){
        var sreviewsSection = document.createElement("section");
        sreviewsSection.className = "sreviews";

        var fromBotDiv1 = document.createElement("div");
        fromBotDiv1.className = "from-bot";

        var questionParagraph = document.createElement("p");
        questionParagraph.textContent = `${que}`;
        // console.log("que: "+que)//please don't delete, for testing

        fromBotDiv1.appendChild(questionParagraph);
        sreviewsSection.appendChild(fromBotDiv1);
        toDoButtonsDiv.appendChild(sreviewsSection);
    });
    

    // Create links
    obj.links.forEach(function (link) {
        var sreviewsSection = document.createElement("section");
        sreviewsSection.className = "sreviews";

        var linkElement = document.createElement("a");
        linkElement.setAttribute("class", "");
        linkElement.setAttribute("href", link["url"]);
        linkElement.textContent = `${link["name"]}`;

        const fromBotDiv = document.createElement("div");
        fromBotDiv.setAttribute("class", "from-bot");
        fromBotDiv.appendChild(linkElement);

        sreviewsSection.appendChild(fromBotDiv);
        toDoButtonsDiv.appendChild(sreviewsSection)
    });

    buttonsDiv = createButtons(obj);
    toDoButtonsDiv.appendChild(buttonsDiv)

    // Append result
    contentBlock.appendChild(toDoButtonsDiv);
}

function scrollToBottomSmoothly(duration) {
    const element = document.querySelector(".wrapper_modal-content");
    const scrollHeight = element.scrollHeight;
    const startPosition = element.scrollTop;
    const startTime = performance.now();

    function scrollAnimation(currentTime) {
        const elapsedTime = currentTime - startTime;
        if (elapsedTime < duration) {
            const progress = elapsedTime / duration;
            element.scrollTop = startPosition + progress * (scrollHeight - startPosition);
            requestAnimationFrame(scrollAnimation);
        } else {
            element.scrollTop = scrollHeight;
        }
    }

    requestAnimationFrame(scrollAnimation);
}

let choiceStack = [];
let currentIndex = -1;

function ButtonBack() {
    if (currentIndex > 0) {
        currentIndex--;
        const prevChoice = choiceStack[currentIndex];
        navigateToChoice(prevChoice);
    } else {
        currentIndex = -1;
        choiceStack = [];
        navigateToChoice("main_1");
    }
}

function navigateToChoice(choiceId) {
    //console.log("navigate currentIndex: "+currentIndex)//please don't delete, for testing
    //console.log("navigate choiceStack: "+choiceStack)//please don't delete, for testing

    if (choiceId === "back") {
        ButtonBack();
        scrollToBottomSmoothly(1000);
    }

    const selectedChoice = data[choiceId];

    if (selectedChoice) {
        if (selectedChoice.type == "link") {
            createLinks(selectedChoice);
        } else if (selectedChoice.type == "question") {
            createToDoButtons(selectedChoice);
        } else if (selectedChoice.type == "question_link"){
            createQuestionLink(selectedChoice);
        }
        //console.log(selectedChoice)//please don't delete, for testing
    }
}

//// The main function ////
function my_function() {
    //console.log("my_function currentIndex: "+currentIndex)//please don't delete, for testing
    //console.log("my_function choiceStack:"+choiceStack)//please don't delete, for testing

    const buttons = document.querySelectorAll(".button");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            //console.log("clicked on  "+button.textContent)//please don't delete, for testing

            const choiceId = button.getAttribute("id");

            if (choiceId != "back") {
                // for every not back button
                choiceStack = choiceStack.slice(0, currentIndex + 1);
                currentIndex++;
                choiceStack.push(choiceId);

                showUserChoise(button.textContent);
                navigateToChoice(choiceId)

            }else{
                //for every button back
                showUserChoise(button.textContent);
                ButtonBack()
            }

            scrollToBottomSmoothly(1000);
            my_function();

            
        });
    });
}


my_function();

/*
Потуга №1

function ButtonBack(previousId, previousOptions) {
    // createToDoButtons(previousObj);
    // var previousObj = findNextInfo(data, previousId);
    // if (previousObj) {
    //     if (previousObj["type"] == "link") {
    //         createLinks(previousObj);
    //     } else if (previousObj["type"] == "question"  previousObj["type"] == "question_link") {
    //         createToDoButtons(previousObj);
    //         if (previousObj["type"] == "question") {
    //             // previousOptions.pop(); // Remove the last option from previousOptions
    //         }
    //     }
    //     scrollToBottomSmoothly(1000);
    //     my_function();
    // }
    var buttonBack = document.getElementById('back')


    //var contentBlock = document.querySelector('.modal-content');

    // var backButtonDiv = document.createElement("div");
    // backButtonDiv.className = "back-button";

    // var backButton = document.createElement("button");
    // backButton.className = "button-back";
    // backButton.textContent = "Назад ↩️";
    buttonBack.addEventListener("click", function () {
        // contentBlock.innerHTML = ""; // Clear the content
        //console.log('ololo')

        // showUserChoise("Назад ↩️");
        var previousObj = findNextInfo(data, previousId);
        if (previousObj) {
            if (previousObj["type"] == "link") {
                createLinks(previousObj);
            } else if (previousObj["type"] == "question" || previousObj["type"] == "question_link") {
                createToDoButtons(previousObj);
                if (previousObj["type"] == "question") {
                    // previousOptions.pop(); // Remove the last option from previousOptions
                }
            }
            scrollToBottomSmoothly(1000);
            my_function();
        }
    });

    // backButtonDiv.appendChild(backButton);
    // contentBlock.appendChild(backButtonDiv);
}
let previousOptions = [];

function my_function() {
    const buttons = document.querySelectorAll(".button");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            showUserChoise(button.textContent);
            console.log(previousOptions)
            obj = findNextInfo(data, button.getAttribute("id"));

            debugger
            if (previousOptions.length > 0) {
                ButtonBack(previousOptions[previousOptions.length - 1], previousOptions);
            } else {
                previousOptions.push('main_1')
            }

            console.log(obj) //TODO testing
            if (obj) {
                if (obj["type"] == "link") {
                    console.log("It's a link"); //TODO testing
                    createLinks(obj);
                    previousOptions.push(button.getAttribute("id")); // Store the current option ID
                    const prev_id = previousOptions[0];
                    ButtonBack(prev_id, previousOptions);

                } else if (obj["type"] == "question") {
                    console.log("It's a question"); //TODO testing
                    createToDoButtons(obj);
                    previousOptions.push(button.getAttribute("id")); // Store the current option ID
                    const prev_id = previousOptions.length >= 2
                        ? previousOptions[previousOptions.length - 2]
                        : previousOptions[0];
                    ButtonBack(prev_id, previousOptions);
                } else if (obj["type"] == "question_link") {
                    console.log("It's a question with links"); //TODO testing
                    // function for this type
                    previousOptions.push(button.getAttribute("id")); // Store the current option ID
                    ButtonBack(button.getAttribute("id"), previousOptions);
                }

                scrollToBottomSmoothly(1000);
                my_function(); // restart the function to add eventlistener for new buttons
            }
        });
    });
}

my_function();
*/