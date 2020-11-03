document.onreadystatechange = function() { 
    if (document.readyState !== "complete") { 
        document.querySelector( 
          "body").style.visibility = "hidden"; 
        document.querySelector( 
          "#icon").style.visibility = "visible"; 
    } else { 
        document.querySelector( 
          "#icon").style.display = "none"; 
        document.querySelector( 
          "body").style.visibility = "visible"; 
    } 
}; 