# Given an image of a guide, extract the text using pytesseract

import pytesseract 
from PIL import Image 

def get_text(filename): 

    print(pytesseract.image_to_string(Image.open('md.png')))
    guide_text = pytesseract.image_to_string(Image.open('md.png'))
    
    print(pytesseract.image_to_string('md.png'))
    return guide_text 
