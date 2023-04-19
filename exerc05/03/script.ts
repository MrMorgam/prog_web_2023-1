const botao1: HTMLElement = document.getElementById("botao1");
const botao2: HTMLElement = document.getElementById("botao2");

botao1.addEventListener("click", function() {
    const paragrafo: HTMLElement = document.getElementById("paragrafo");
    paragrafo.textContent = "O texto deste parágrafo foi alterado!";
});


botao2.addEventListener("click", function() {
    const paragrafo: HTMLElement = document.getElementById("paragrafo");
    paragrafo.textContent = "";
});