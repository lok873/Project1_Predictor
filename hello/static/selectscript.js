
function dropdown(obj){
           var data = $(obj.element).data();
            var text = $(obj.element).text();
           
            
if(data && data['img_src']){
   img_src = data['img_src'];                      
     template = $("<div><img src=\"" + img_src + "\" style=\"width:20%;height:15px;\"/><p style=\" display:inline ; white-space :nowrap ; font-weight: 700;font-size:10pt;text-align-last:right;\">" + text + "</p></div>"); return template;     }                                                   }                                             
     
     var o = {   
        'templateResult': dropdown,

}
$('#c1').select2(o);
$('#c2').select2(o);


   

   