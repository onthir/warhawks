// submit message
$(document).ready(function() {
    $('#contactForm').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                $("#contactForm")[0].reset(); // update the DIV
            }
        });
        return false;
    });
});

// dropdown trigger for navbar
$('.dropdown-trigger').dropdown();

// select materialize trigger
$(document).ready(function(){
    $('select').formSelect();
});

// date picker trigger

$(document).ready(function(){
$('.datepicker').datepicker();
});
