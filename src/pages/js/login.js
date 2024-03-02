$(document).ready(function() {
  $("#loginForm").submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting traditionally
    var formData = {
      username: $("#email").val(),
      password: $("#password").val(),
      grant_type: "",
      scope: "",
      client_id: "",
      client_secret: ""
    };
    $.ajax({
      type: "POST",
      url: "https://localhost:8000/auth/jwt/login",
      data: formData,
      dataType: "json",
      success: function(response) {
        console.log(response);
        window.location.href = "/";
        // Handle successful login, maybe redirect to another page
      },
      error: function(xhr, status, error) {
        console.error(xhr.responseText);
        // Handle login errors, display message to user, etc.
      }
    });
  });
});