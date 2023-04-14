function setvar() {
    var cutbutton = document.getElementById("cutbox");
    cutbutton.addEventListener('click', disablebutton(cutbutton));
}
  
function disablebutton(cutbutton){
    var darkElements = document.getElementsByClassName("dark");
    console.log(darkElements);

    for (var i = 0; i < darkElements.length; i++) {
        if(cutbutton.checked) {
            darkElements[i].disabled = false;
        }
        if(!cutbutton.checked) {
            darkElements[i].disabled = true;
            darkElements[i].checked = false;
        }
    }
}

function formmagic() {
    setvar();
}

document.addEventListener("DOMContentLoaded", formmagic)