
var mini = true;
var toggle = true;

function toggleSidebar() {
  if (mini) {
    document.getElementById("mySidebar").style.width = "250px";
    var sidebarTextElements = document.getElementsByClassName("sidebar-text");
    for (var i = 0; i < sidebarTextElements.length; i++) {
      sidebarTextElements[i].classList.add("show-sidebar-text");
    }
    mini = false;

  } else {
    document.getElementById("mySidebar").style.width = "60px";
    var sidebarTextElements = document.getElementsByClassName("sidebar-text");
    for (var i = 0; i < sidebarTextElements.length; i++) {
      sidebarTextElements[i].classList.remove("show-sidebar-text");
    }
    mini = true;
  
  }
}

function clickSidebar() {
  if (toggle) {
    document.getElementById("mySidebar").style.width = "250px";
    var sidebarTextElements = document.getElementsByClassName("sidebar-text");
    for (var i = 0; i < sidebarTextElements.length; i++) {
      sidebarTextElements[i].classList.add("show-sidebar-text");
    }
    toggle = false;
  } else {
    document.getElementById("mySidebar").style.width = "60px";
    var sidebarTextElements = document.getElementsByClassName("sidebar-text");
    for (var i = 0; i < sidebarTextElements.length; i++) {
      sidebarTextElements[i].classList.remove("show-sidebar-text");
    }
    toggle = true;
  }
}



  
  