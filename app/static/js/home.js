
function homeSubmit()
{
  debugger;  
  // Get the form data
  var myForm = $("#homeForm")
  var form_data = myForm.serialize();
  
  // Send the form data to the server as an AJAX request
  $.ajax({
      url: '/app/index/home/submit/',
      type: 'POST',
      data: form_data,
      success: function(data) {
          // Handle the response from the server
          debugger;
          console.log(data);
      },
      error: function(xhr, status, error) {
        debugger
        // Handle error response
      }
  });
}