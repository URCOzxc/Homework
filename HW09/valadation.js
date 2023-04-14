document.addEventListener("DOMContentLoaded", function() {
    var cutbutton = document.getElementById("cutbox");
  
    function disablebutton() {
      var darkElements = document.getElementsByClassName("dark");
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
  
    cutbutton.addEventListener('click', disablebutton);
  });