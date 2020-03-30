from PIL import ImageGrab
from PIL import Image
import pytesseract
bbox = (1120, 50, 1600, 650)
im = ImageGrab.grab(bbox) #可以添加一个坐标元组进去
im.save('E:\\12.png')
text=pytesseract.image_to_string(Image.open('E:\\12.png'),'chi_sim')
# abc = text.split("\n")
print(text);
im.show()