const botao1: HTMLElement = document.getElementById("b1");
const botao2: HTMLElement = document.getElementById("b2");
 

botao1.addEventListener("click", function() {
    document.body.style.color = "white";
    document.body.style.backgroundColor = "black";
});

botao2.addEventListener("click", function() {
    document.body.style.color = "black";
    document.body.style.backgroundColor = "white";
});