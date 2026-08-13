const heading = document.querySelector("h1");
console.log(heading);
heading.textContent = "Hello, Ryan!";
const button = document.querySelector("button");
button.addEventListener("click", function () {
    alert("Thanks for reaching out!");
});