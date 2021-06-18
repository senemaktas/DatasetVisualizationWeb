function onayla(){

  var x=document.forms['form1'][0].value;
  var y=document.forms['form1'][1].value;
  var z=document.forms['form1'][2].value;
  var t=document.forms['form1'][3].value;

  
   if ( (x==null) && (y==null) && (z==null) && (t==null)){
       alert("Please fill out all inputs!!!");			 
       return true;
   }
 else{
      // Popup Al
  var modal = document.getElementById('disPopId');
  
  // Kipi açan düğmeyi al
  var btn = document.getElementById("submitid");
  
  // Kipi kapatan <span> öğesini edinin
  var span = document.getElementsByClassName("close")[0];
  
  // Kullanıcı düğmeyi tıklattığında
  btn.onclick = function() {
      modal.style.display = "block";
  }
  
  // Kullanıcı <span> (x) düğmesini tıkladığında, popup
  span.onclick = function() {
      modal.style.display = "none";
  }
  
  // Kullanıcı modelden başka herhangi bir yeri tıklattıysa, onu kapatın.
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }	 
     return false;
  }	
}	

function butonDataset(){
 
 // Popup Al
  var modal = document.getElementById('disPopId');
  
  // Kipi açan düğmeyi al
  var btn = document.getElementById("submitid");
  
  // Kipi kapatan <span> öğesini edinin
  var span = document.getElementsByClassName("close")[0];
  
  // Kullanıcı düğmeyi tıklattığında
  btn.onclick = function() {
      modal.style.display = "block";
  }
  
  // Kullanıcı <span> (x) düğmesini tıkladığında, popup
  span.onclick = function() {
      modal.style.display = "none";
  }
  
  // Kullanıcı modelden başka herhangi bir yeri tıklattıysa, onu kapatın.
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }	 
     return false;
  }

// this part is uploading file ---------------------------------------
    $("#file-picker").change(function(){

    var input = document.getElementById('file-picker');

    for (var i=0; i<input.files.length; i++)
    {
    //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
    var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()

    if ((ext == 'xml') || (ext == 'csv'))
    {
        $("#msg").text("Files are supported")
    }
    else
    {
        $("#msg").text("Files are NOT supported")
        document.getElementById("file-picker").value ="";
    }
    } } );
