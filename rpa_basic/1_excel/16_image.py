from openpyxl import Workbook
from openpyxl.drawing.image import Image
#from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

wb = Workbook()
ws = wb.active

img = Image("image.png")

#img = Image.open('image.png')

ws.add_image(img, "C3")

wb.save("sample_image.xlsx")