let cutbutton = null;

function setvar() {
    cutbutton = document.getElementById("cutbox");
}

function disablebutton() {
    if(cutbutton.checked) {
        document.getElementsByClassName("dark").disabled = false;
    }
    if(!cutbutton.checked) {
        document.getElementsByClassName("dark").disabled = true;
    }
}

document.addEventListener('load', setvar());
cutbutton.addEventListener('click', disablebutton());