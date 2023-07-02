 // Counter to keep track of the number of duplicated forms
 let formCounter = 1;

 // Function to duplicate the form
 function duplicateForm() {
   const form = document.querySelector('.border.rounded-3.bg-light'); // Select the form element to duplicate
   const clonedForm = form.cloneNode(true); // Clone the form element
   const addButton = document.getElementById('addForm'); // Select the add form button

   // Update the IDs of the cloned form fields to ensure uniqueness
   const clonedFormFields = clonedForm.querySelectorAll('input, select');
   clonedFormFields.forEach(field => {
     const fieldName = field.getAttribute('name');
     if (fieldName) {
       field.setAttribute('name', `${fieldName}-${formCounter}`);
       field.value = ''; // Clear the field value in the cloned form
     }
   });

   // Insert the cloned form after the last form
   form.parentNode.insertBefore(clonedForm, addButton);

   formCounter++; // Increment the form counter
 }

 // Add event listener to the add form button
 const addFormButton = document.getElementById('addForm');
 addFormButton.addEventListener('click', duplicateForm);