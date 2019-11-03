import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
import PIL
from PIL import Image

a = []

with open('saved.txt', 'r') as f:
    for l in f:
        a.append(l)


b = []

for i in a:
    b.append(i.replace('\n', ''))

x = []
y = []
z = []

j = 0
for i in b:
    if j % 3 == 0:
        x.append(float(i))
    elif j % 3 == 1:
        y.append(float(i))
    elif j % 3 == 2:
        z.append(float(i))
    j += 1

n = []

for i in z:
    if i == 0:
        n.append("FIFO")
    else:
        n.append("RR")

print(x)
print(y)

plt.plot(x, y, 'ro')

for i, txt in enumerate(n):
    plt.annotate(txt,(x[i],y[i]))
plt.savefig('d.png')

wpercent = 0.5
img = Image.open('d.png')
hsize = int((float(img.size[1]) * float(wpercent)))
wsize = int((float(img.size[0]) * float(wpercent)))
img = img.resize((wsize, hsize), PIL.Image.ANTIALIAS)
img.save('d.png')
