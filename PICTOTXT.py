import pytesseract
from PIL import Image

img = Image.open('D:/PYTHONS/IMG2TXT/PYTESSLOC.jpg')


#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\'
# Recognize text with tesseract for python
res = pytesseract.image_to_string(img)

print(res)  
