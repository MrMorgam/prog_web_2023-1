document.addEventListener('DOMContentLoaded', function () {
    var botaoOK = document.getElementById('botaoOK');
    botaoOK.addEventListener('click', exibirImg);
});

function exibirImg() {
    var conteudo = document.getElementById('textoDeEntrada').value;

    if (conteudo != 'imagem') {
        alert('Nome da imagem inválido!');
    } else {
        document.getElementById('resultado').innerHTML = ''
        const imagem = document.createElement('img');
        imagem.src='./imagens/' + conteudo + '.jpg';

        document.getElementById('resultado').appendChild(imagem);
    }
}