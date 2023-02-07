from pytesseract import pytesseract
from PIL import Image

#site tesseract.exe: https://github.com/UB-Mannheim/tesseract/wiki 

path_to_tesseract = r"PATH\TESSERACT.EXE"
image_path = r"IMAGE PATH"
img = Image.open(image_path) 
pytesseract.tesseract_cmd = path_to_tesseract 
  
text = pytesseract.image_to_string(img) 
print(text[:-1])