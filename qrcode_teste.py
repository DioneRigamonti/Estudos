import qrcode

#Criando um QrCode para acessar o site do YouTube

imagem = qrcode.make('https://www.youtube.com/') # adicionando p link em uma variavel.
imagem.save('Primeira_imagem.jpg') # salvando a imagem na mesma pasta que o arquivo em formato jpg (pode ser em qualquer formato)

print('Fim')