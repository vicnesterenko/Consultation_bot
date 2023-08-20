const menu = document.querySelector(".menu");
const menuItems = document.querySelectorAll(".menuItem");
const hamburger= document.querySelector(".hamburger");
const closeIcon= document.querySelector(".closeIcon");
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
  function(menuItem) { 
    menuItem.addEventListener("click", toggleMenu);
  }
)


/////////////////////////////////////////////////////

function showUserChoise(text) {
  //var buttonText = button.textContent;

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

// Add an event listener to each button
document.querySelectorAll(".button").forEach(function (button) {
  button.addEventListener("click", function () {
      showUserChoise(button.textContent);
      /////////////////////////////////////////////////////

});
});