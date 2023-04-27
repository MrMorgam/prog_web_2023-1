document.addEventListener('DOMContentLoaded', function () {
    var botaoOK = document.getElementById('botaoOK');
    botaoOK.addEventListener('click', exibirImg());
});

function exibirImg() {
    document.getElementById('resultado').innerHTML = ''

    var conteudo = document.getElementById('imagens').value;

    var imagem = document.createElement('img');
    imagem.src = './imagens/' + conteudo + '.jpg';

    document.getElementById('resultado').appendChild(imagem);
}