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

function createButtons(obj, name) {
    console.log("Object from button: ");
    console.log(obj);

    var buttonsDiv = document.createElement("div");
    buttonsDiv.className = "buttons";
    // Loop through the options and create buttons
    obj.options.forEach(function (option) {
        var button = document.createElement("button");

        button.id = option.next_id;
        // button.name = name;
        button.classList.add(name);

        if (button.id == "manager") {
            button.classList.add("button-manager", "button");
            button.title = "Зв'язатись з менеджером";
        } else if (button.id == "back") {
            button.classList.add("button-prev", "button");
        } else if (button.id == "main_1") {
            button.classList.add("button-main", "button");
        } else {
            button.className = "button";
        }

        button.textContent = option.label;

        buttonsDiv.appendChild(button);
    });
    return buttonsDiv;
}

var scriptElement = document.getElementById("external-js-script");
var staticBaseUrl = scriptElement.getAttribute("data-static-url");

function createToDoButtons(obj, choiceId) {
    console.log("Object from Question:")
    console.log(obj)

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

    buttonsDiv = createButtons(obj, choiceId);

    if (obj.img) {
        console.log(obj);
        var imageDiv = document.createElement("div");

        // Create a new image element
        var image = document.createElement("img");
        src = "/static/" + obj.img + ""
        image.setAttribute("src", src);
        image.setAttribute("width", "200px");
        image.setAttribute("height", "200px");
        image.setAttribute("title", "image 14");

        imageDiv.appendChild(image);

        imageDiv.className = "img-div";

        toDoButtonsDiv.appendChild(imageDiv);
    }

    toDoButtonsDiv.appendChild(sreviewsSection);
    toDoButtonsDiv.appendChild(buttonsDiv);

    contentBlock.appendChild(toDoButtonsDiv);
}

function createLinks(obj, choiceId) {
    var contentBlock = document.querySelector('.modal-content');

    var toDoButtonsDiv = document.createElement("div");
    toDoButtonsDiv.className = "to-do-buttons";

    var i = 0;
    obj.texts.forEach(function (text) {
        var sreviewsSection = document.createElement("section");
        sreviewsSection.className = "sreviews";

        var linkElement = document.createElement("a");
        linkElement.setAttribute("class", "");
        linkElement.setAttribute("href", text["url"]);
        linkElement.textContent = `${i + 1}. ${text["name"]}`;
        const fromBotDiv = document.createElement("div");
        fromBotDiv.setAttribute("class", "from-bot");
        fromBotDiv.appendChild(linkElement);
        i = i + 1;

        sreviewsSection.appendChild(fromBotDiv);
        toDoButtonsDiv.appendChild(sreviewsSection);
    });

    if (obj.img) {
        console.log(obj);
        var imageDiv = document.createElement("div");
        imageDiv.className = "img-div";
        imageDiv.innerHTML = obj.img;
        toDoButtonsDiv.appendChild(imageDiv);
    }

    buttonsDiv = createButtons(obj, choiceId);

    toDoButtonsDiv.appendChild(buttonsDiv);
    contentBlock.appendChild(toDoButtonsDiv);
}

function createQuestionLink(obj, choiceId) {
    console.log("Object from QuestionLinks:")
    console.log(obj)

    var contentBlock = document.querySelector('.modal-content');

    var toDoButtonsDiv = document.createElement("div");
    toDoButtonsDiv.className = "to-do-buttons";

    // Create first message/messages
    obj.q.forEach(function (que) {
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

    // if (obj.img){
    //     console.log(obj);
    //     var imageDiv = document.createElement("div");
    //     imageDiv.className = "img-div";
    //     imageDiv.innerHTML = obj.img;
    //     toDoButtonsDiv.appendChild(imageDiv);}

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

    buttonsDiv = createButtons(obj, choiceId);
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


    // console.log("choiceId " + choiceId);
    // console.log(data);

    const selectedChoice = data[choiceId];

    if (selectedChoice) {
        if (selectedChoice.type == "link") {
            createLinks(selectedChoice, choiceId);
        } else if (selectedChoice.type == "question") {
            createToDoButtons(selectedChoice, choiceId);
        } else if (selectedChoice.type == "question_link") {
            createQuestionLink(selectedChoice, choiceId);
        }
    }
}
// VIDEO DISPLAY ADDING BY API YOUTUBE
const jsonData = {
    "elements": [
        {
            "id": "praktyka_main",
            "eventType": "click",
            "handler": "displayYouTubeVideoInfo"
        }
        // Add more elements as needed
    ]
};

// Function to fetch YouTube video information
async function fetchYouTubeVideoInfo() {
    const apiKey = 'AIzaSyAsnWOIa_Qp_pWuAENqAi2AYCxtuwoIJcE'; // Use your API key
    const channelId = 'UC7M-0zfJr5dsgiW7PGZno8A'; // Channel ID without "@" symbol
    const apiUrl = `https://www.googleapis.com/youtube/v3/search?key=${apiKey}&channelId=${channelId}&order=date&part=snippet&type=video&maxResults=10`;

    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`Network response was not ok (${response.status} ${response.statusText})`);
        }

        const data = await response.json();

        if (data.items && data.items.length > 0) {
            const video = data.items[0];
            const videoId = video.id.videoId;
            const videoTitle = video.snippet.title;
            const videoThumbnail = video.snippet.thumbnails.medium.url;

            return { videoId, videoTitle, videoThumbnail };
        } else {
            console.log('No videos found.');
            return null;
        }
    } catch (error) {
        console.error('Error fetching YouTube video information:', error);
        return null;
    }
}

// Function to display video information in the chatbot
// ... (Previous code)

// Function to display video information in the chatbot
function displayYouTubeVideoInfo() {
    fetchYouTubeVideoInfo().then(videoInfo => {
        if (videoInfo) {
            const contentBlock = document.querySelector('.modal-content');

            // Create elements for video info (thumbnail, title, link)
            const videoDiv = document.createElement('div');
            const videoLink = document.createElement('a');
            const videoImage = document.createElement('img');
            const videoTitle = document.createElement('p');
            const videoIframe = document.createElement('iframe'); // Add this line

            videoLink.href = `https://www.youtube.com/watch?v=${videoInfo.videoId}`;
            videoLink.target = '_blank';
            videoImage.src = videoInfo.videoThumbnail;
            videoImage.alt = videoInfo.videoTitle;
            videoTitle.textContent = videoInfo.videoTitle;

            videoIframe.src = `https://www.youtube.com/embed/${videoInfo.videoId}`; // Set iframe src
            videoIframe.width = '560'; // Set iframe width
            videoIframe.height = '315'; // Set iframe height
            videoIframe.allowfullscreen = true; // Allow fullscreen

            videoLink.appendChild(videoImage);
            videoDiv.appendChild(videoLink);
            videoDiv.appendChild(videoTitle);
            videoDiv.appendChild(videoIframe); // Append the iframe to the videoDiv

            contentBlock.appendChild(videoDiv);
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    jsonData.elements.forEach(elementData => {
        const element = document.getElementById(elementData.id);

        if (element) {
            element.addEventListener(elementData.eventType, window[elementData.handler]);
        }
    });
});



//// The main function ////
function main() {
    //console.log("main currentIndex: "+currentIndex)//please don't delete, for testing
    //console.log("main choiceStack:"+choiceStack)//please don't delete, for testing

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

            }
            else {
                //for every button back
                showUserChoise(button.textContent);
                ButtonBack()
            }

            scrollToBottomSmoothly(1000);
            main();

        });
    });
    const backToMainButton = document.getElementById("backToMainButton");

    backToMainButton.addEventListener("click", function () {
        currentIndex = -1;
        choiceStack = [];
        navigateToChoice("main_1");
        scrollToBottomSmoothly(1000);
    });
}


main(); 