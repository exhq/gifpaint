#!/usr/bin/python3
from collections import namedtuple
import sys
from PIL import Image as image
from PIL import ImageSequence
if len(sys.argv) < 2:
    exit()

dur = 50

argsinfo = namedtuple(
    "argsinfo" , "function usage"
)

def ddur(number):
    global dur
    dur = int(number)



def togif(location):
    ims = []
    img = image.open(location)
    imagecount = img.size[1]//img.size[0]
    for i in range(imagecount):
        ims.append(img.copy().crop((0, img.size[0]*i, img.size[0], img.size[0]*(i+1))))       
    ims[0].save("output.gif", save_all=True, append_images=ims[1:], loop=0, duration=dur, disposal=2)

def topng(location):
    img = image.open(location)
    res = [img.size[0], img.size[1]*img.n_frames]
    output = image.new(mode="RGBA", size=res)
    outputpain = output.load()
    width, height = img.size
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        pix = frame.convert("RGBA").load()
        for ver in range(width):
            for hor in range(height):
                outputpain[ver,hor+(height*(i))] = pix[ver,hor]
    output.save("output.png")

balls = {
    "-d" : argsinfo(ddur, "lmfao this isnt used"),
    "-p" : argsinfo(topng, "filelocation"),
    "-g" : argsinfo(togif, "filelocation")

}

i = 1
while i < len(sys.argv):
    flag = sys.argv[i]
    info = balls.get(flag)
    if info == None:
        print("wrong flag")
        exit()
    argument = sys.argv[i+1]
    info.function(argument)
    i += 2 
