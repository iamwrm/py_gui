import PIL
from PIL import Image

wpercent = 0.005
img = Image.open('1.png')
hsize = int((float(img.size[1]) * float(wpercent)))
wsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
img.save('c1.png')