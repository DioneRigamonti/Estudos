from pytesseract import pytesseract
from PIL import Image

# instale a biblioteca Pillow = pip install Pillow
# instale a biblioteca tesseract = pip install tesseract
#site tesseract.exe: https://github.com/UB-Mannheim/tesseract/wiki 
#quando for instalar o .exe do tesseract...incluir a linguagem portugues para ler o ''Ç''

caminho_tesseract_exe = r"caminho__tesseract_instalado\TESSERACT.EXE"
caminho_imagem = r"caminho_imagem"
abrir_imagem = Image.open(caminho_imagem) 
pytesseract.tesseract_cmd = caminho_tesseract_exe 
  
texto = pytesseract.image_to_string(abrir_imagem,lang='por') 

print(texto)