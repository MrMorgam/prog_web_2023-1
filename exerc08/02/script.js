document.addEventListener('DOMContentLoaded', function () {
    var botaoCalcular = document.getElementById('botaoCalcular');
    botaoCalcular.addEventListener('click', exibirSoma);
});

function exibirSoma() {
    var numero1 = Number(document.getElementById('numero1').value);
    var numero2 = Number(document.getElementById('numero2').value);
    var soma = numero1 + numero2;
    
    if (isNaN(soma)) {
        alert("Erro: número inválido")
    } else {
        document.getElementById('resultado').innerHTML = "Resultado: " + soma;
    }
   
}