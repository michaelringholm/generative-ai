$(document).ready(function() {
    // When the button is clicked
    $('#generate-response-btn').click(function(e) {
      generateResponse();
    });
  });

  function generateResponse() {
    //e.preventDefault(); // Prevent the default form submission
    console.log("generateResponse() called...");
  
      // Get the input values
      var prompt = $('#prompt').val();
      var llm = $('#llm').val();
  
      // Make a POST request to the backend API
      $.ajax({
        url: '/api/generateResponse',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ prompt: prompt, llm: llm }),
        success: function(response) {
          console.log(response);
          $("#generated_response").text(response.generated_response);
        },
        error: function(error) {
          // Handle any errors that occur during the API request
          console.error(error);
        }
      });
  }

  function printUserMessage(message) {
    var userMessageElement = $('<div>').addClass('user-message').text(message);
    $('.chat-container').append(userMessageElement);
  }

  function printAssistantMessage(message) {
    var assistantMessageElement = $('<div>').addClass('assistant-message').text(message);
    $('.chat-container').append(assistantMessageElement);
  }

  // Example usage
  //printUserMessage("Hello!");
  //printAssistantMessage("Hi there! How can I assist you?");
  