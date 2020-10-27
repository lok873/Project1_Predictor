$(document).ready(function() {
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
});



var countries = {
  "India" : ".ind",
  "Australia" : ".aus",
  "England" : ".eng",
  "NewZealand" : ".nz",
  "SouthAfrika" : ".sa",
  "WestIndies" : ".wi",
  "Pakistan" : ".pak",
  "SriLanka" : ".sl",
  "Bangladesh" : ".ban",
  "Afganistan" : ".afg"

}

function getValue1(obj){
   var sel1= (obj.value);
   
   var counval = countries[sel1];

  for(var key in countries) {
  var dictvalue = countries[key];
  var hidden1 = 'select[name="player1"] '.concat(dictvalue);
  var hidden2 = 'select[name="player2"] '.concat(dictvalue);
  var hidden3 = 'select[name="player3"] '.concat(dictvalue);
  var hidden4 = 'select[name="player4"] '.concat(dictvalue);
  var hidden5 = 'select[name="player5"] '.concat(dictvalue);
  var hidden6 = 'select[name="player6"] '.concat(dictvalue);
  var hidden7 = 'select[name="player7"] '.concat(dictvalue);
  var hidden8 = 'select[name="player8"] '.concat(dictvalue);
  var hidden9 = 'select[name="player9"] '.concat(dictvalue);
  var hidden10 = 'select[name="player10"] '.concat(dictvalue);
  var hidden11 = 'select[name="player11"] '.concat(dictvalue);
  

  var hide={
    1 : hidden1,
    2 : hidden2,
    3 : hidden3,
    4: hidden4,
    5 : hidden5,
    6 : hidden6,
    7 : hidden7,
    8 : hidden8,
    9 : hidden9,
    10 : hidden10,
    11 : hidden11
  }


  for(var key2 in hide){

  $(hide[key2]).hide();
  
  }
  
}
$(counval).show();

}


function getValue2(obj){
   var sel2= (obj.value);
   console.log(sel2)
}
