//Append nodeText to newElement as a child, and append newElement to parentTag as a child. 

let parentTag = document.getElementById("list");
let newElement = document.createElement("li");
let nodeText = document.createTextNode("Joe");


newElement.appendChild(nodeText);

parentTag.appendChild(newElement);

//Remove the span element from the h2.
document.getElementById("special-h2").removeChild(document.getElementById("delete-text"));


x = 5, 2x
2 * 5 = 10
//Document #1
let thing = "word"
let i = thing

//Document #2
let i = "word"


//Append nodeText to newElement as a child, and append newElement to parentTag as a child. 

("list");


newElement.appendChild(nodeText);

document.getElementById("list").appendChild(document.createElement("li"));

Register the textLength event handler to handle blur changes for the textarea tag. Note: The function counts the number of characters in the textarea.

let textareaElement = document.getElementById("studentName");

function textLength(event) {
   document.getElementById("stringLength").innerHTML = event.target.value.length;
}

textarea.textLength("blur");



let inputElement = document.getElementById("studentName"); function textSize(event) { 
    document.getElementById("stringLength").innerHTML = event.target.value.length; 
 } ;
 
 inputElement.addEventListener("input", textSize);

 //Register the textSize event handler to handle blur changes for the textarea tag. Note: The function counts the number of characters in the textarea. 
/*html: <label for="yourName">Your name:</label>
<textarea id="yourName" cols="40" rows="3"></textarea><br>
<p id="stringLength">0</p>  */

 let textareaElement = document.getElementById("yourName");

 function textSize(event) {
   document.getElementById("stringLength").innerHTML = event.target.value.length;
}

textareaElement.addEventListener("blur", textSize);



//Write and register an event handler that displays "Event handled" on the console log when the h2 element receives a mouseout event

let h2Element = document.getElementsByTagName("h2")[0];

function cl() {console.log("Event handled")}
h2Element.addEventListener("mouseout", cl);


//Write and register an event handler that changes the color of the a tag to red on click. 

let aElement = document.getElementsByTagName("a")[0];




function cl() {
   aElement.style = ("color: red"); 
}
aElement.addEventListener("click", cl);