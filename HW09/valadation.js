function disablebutton() {
    if(document.getElementById("cutbox").checked){
        document.getElementsByClassName("dark").disabled = false;
    }
    if(!document.getElementById("cutbox").checked){
        document.getElementsByClassName("dark").disabled = true;
    }
}