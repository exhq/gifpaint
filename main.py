#!/usr/bin/python3
import sys
from PIL import Image as image
from PIL import ImageSequence

if len(sys.argv) != 2:
    print("usage: pain.py [path of gif]") 
    exit()

img = image.open(sys.argv[1])
res = [img.size[0], img.size[1]*img.n_frames]
output = image.new(mode="RGBA", size=res)
outputpain = output.load()
width, height = img.size
for i, frame in enumerate(ImageSequence.Iterator(img)):
    pix = frame.convert("RGBA").load()
    if i == 0:
        for ver in range(width):
            for hor in range(height):
                outputpain[ver,hor] = pix[ver,hor]

    elif i != 0:
        for ver in range(width):
            for hor in range(height):
                outputpain[ver,hor+(height*(i))] = pix[ver,hor]

print("complete!")
output.save("output.png")
