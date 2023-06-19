  // JavaScript to handle the click event and add/remove the active class
  document.addEventListener('DOMContentLoaded', function() {
    var header = document.getElementById('myHeader');
    var navItems = header.getElementsByClassName('nav-item');

    // Add click event listener to each nav-item
    for (var i = 0; i < navItems.length; i++) {
      navItems[i].addEventListener('click', function() {
        // Remove the active class from all nav-items
        for (var j = 0; j < navItems.length; j++) {
          navItems[j].classList.remove('active');
        }
        
        // Add the active class to the clicked nav-item
        this.classList.add('active');
      });
    }
  });

  function checkInput(input) {
    if (input.value.length > 0) {
      input.placeholder = '';
    } else {
      input.placeholder = 'Search for anything..';
    }
  }
  function adjustPlaceholder(input) {
    input.classList.add('form-control-small');
    input.placeholder = 'Search for anything..';
  }

  $(document).ready(function() {
    $('.carousel').carousel({
      interval: 4000 // Autoplay interval in milliseconds (4 seconds)
    });
  });