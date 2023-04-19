var botao1 = document.getElementById("botao1");
var botao2 = document.getElementById("botao2");
botao1.addEventListener("click", function () {
    var paragrafo = document.getElementById("paragrafo");
    paragrafo.textContent = "O texto deste parágrafo foi alterado!";
});
botao2.addEventListener("click", function () {
    var paragrafo = document.getElementById("paragrafo");
    paragrafo.textContent = "";
});
