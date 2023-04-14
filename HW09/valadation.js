const cutbutton = document.getElementById("cutbox");

function disablebutton() {
    if(cutbutton.checked){
        document.getElementsByClassName("dark").disabled = false;
    }
    if(!cutbutton.checked){
        document.getElementsByClassName("dark").disabled = true;
    }
}

cutbutton.addEventListener('click', disablebutton());