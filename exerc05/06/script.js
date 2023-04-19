var botao1 = document.getElementById("b1");
var botao2 = document.getElementById("b2");
botao1.addEventListener("click", function () {
    document.body.style.color = "white";
    document.body.style.backgroundColor = "black";
});
botao2.addEventListener("click", function () {
    document.body.style.color = "black";
    document.body.style.backgroundColor = "white";
});
