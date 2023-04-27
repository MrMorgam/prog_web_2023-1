document.addEventListener('DOMContentLoaded', function () {
    var imagens = document.getElementById('imagens');
    imagens.addEventListener('change', exibirImg());
});

function exibirImg() {
    document.getElementById('resultado').innerHTML = ''
    var conteudo = document.getElementById('imagens').value;

    var imagem = document.createElement('img');
    imagem.src = './imagens/' + conteudo + '.jpg';

    document.getElementById('resultado').appendChild(imagem);
}