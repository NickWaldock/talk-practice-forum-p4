// Timeout function for messages displayed by django
setTimeout(function(){
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);