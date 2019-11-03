import draw

sche = [(0, 0, 0, 0),
        (1, 0, 4.9, 0),
        (2, 4.9, 16.9, 0),
        (3, 16.9, 32.4, 0),
        (4, 32.4, 40, 0)]

#cont = {0: {0, 1, 2, 3, 4, 5, 9, 10}, 1: {6, 7, 8, 11, 12}}
#cont = {0: {0, 1, 2, 3, 4, 5, 9, 10,6, 7, 8, 11, 12}}
cont = {0: {0},1:{1},2:{2}}
for i in range(5):
    cont[i]={i}

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

draw.draw_canvas(sche, cont, 'a.png')

# rgbstr='aabbcc'
# print(tuple(ord(c) for c in rgbstr.decode('hex')))


