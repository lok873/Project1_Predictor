
window.onload = disabling; 

function disabling(){
var $selects = $('select');
$selects.on('change', function() {
    $("option", $selects).prop("disabled", false);
    
    $selects.each(function() {
        var $select = $(this), 
            $options = $selects.not($select).find('option'),
            selectedText = $select.children('option:selected').text();
        $options.each(function() {
            if($(this).text() == selectedText) $(this).prop("disabled", true);
        $(".sel").prop("disabled",true);});
        
    $(".sel").prop("disabled",true);});

$(".sel").prop("disabled",true);});



$selects.eq(0).trigger('change');
        }