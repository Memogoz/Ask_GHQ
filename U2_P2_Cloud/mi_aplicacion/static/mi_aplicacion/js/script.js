function resetearChat(){
    let chatHtml = document.getElementById("chat");
    chatHtml.innerHTML = "";
}

function mostrarLoader(){
    let loaderHtml = document.getElementById("loader");
    loaderHtml.style.display = "block";
}