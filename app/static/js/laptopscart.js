  // Get the current page URL
  var currentUrl = window.location.pathname;

  // Get all breadcrumb items
  var breadcrumbItems = document.querySelectorAll('.breadcrumb-item');

  // Loop through each breadcrumb item
  for (var i = 0; i < breadcrumbItems.length; i++) {
    var item = breadcrumbItems[i];

    // Check if the item's link URL matches the current page URL
    if (item.firstChild.getAttribute('href') === currentUrl) {
      // Add the 'active' class to the current page item
      item.classList.add('active');
    } else {
      // Remove the 'active' class from other items
      item.classList.remove('active');
    }
  }