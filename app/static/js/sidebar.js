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

function clickSidebar(event) {
  // Check if the clicked element has the "chevron" class (arrow)
  if ($(event.target).hasClass('chevron')) {
      // Prevent the default behavior (navigation)
      event.preventDefault();

      // Toggle the collapse state for the clicked category
      var category = $(event.currentTarget).closest('li');
      category.find('.collapse').toggleClass('show');
  }
}