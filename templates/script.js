$(document).ready(function() {
    $('#speechButton').click(function() {
        $.ajax({
            type: 'POST',
            url: '/speech-to-text',
            success: function(response) {
                if (response.status === 'listening') {
                    $('#speechButton').css('background-color', '#FF0000');
                    $('#result').text("Listening...");
                } else {
                    $('#speechButton').css('background-color', '#4CAF50');
                    $('#result').text("");
                }
            },
            error: function(xhr, status, error) {
                alert('Error occurred: ' + error);
            }
        });
    });
});
