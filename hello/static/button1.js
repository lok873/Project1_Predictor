

$(document).ready(function() {
    $("#btnFetch").click(function() {
    
    $(this).prop("disabled", false);
    // add spinner to button
    $(this).html(
    '<i class="fa fa-circle-o-notch fa-spin"></i> loading...'
    );
    });
    });