#Name: Joseph Svintsitsky
#Module: Lab 7
#Due Date: 10/17/2021
#Assignment: Write a script that uses that plugin.
#Include at least 3 different usages of the plugin that you’ve selected.
#Resources: https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/index.html#

#Example #1 [UnsharpMask]
from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
    UnsharpMask
    )
simg = Image.open('C:\it3038c-scripts\python\doggo.jpg')

# defaut: radius=2, percent=150, threshold=3
dimg = simg.filter(UnsharpMask(radius=2, percent=150, threshold=3))
dimg.save("C:\it3038c-scripts\python\doggy.jpg")

#Example #2 [Split]
from PIL import Image
#
img = Image.open('C:\it3038c-scripts\python\doggo.jpg')
red, grn, blu = img.split()
red.save("C:\it3038c-scripts\python\_red_doggo.jpg")
grn.save("C:\it3038c-scripts\python\_grn_doggo.jpg")
blu.save("C:\it3038c-scripts\python\_blu_doggo.jpg")
blk = Image.new("L", red.size, "black")

Image.merge("RGB", (red, blk, blk)).save(
    "C:\it3038c-scripts\python\_red_doggo.jpg")
Image.merge("RGB", (blk, grn, blk)).save(
    "C:\it3038c-scripts\python\_grn_doggo.jpg")
Image.merge("RGB", (blk, blk, blu)).save(
    "C:\it3038c-scripts\python\_blu_doggo.jpg")

#Example #3 [Transpose]
from PIL import Image
#
img = Image.open('C:\it3038c-scripts\python\doggo.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save(
    "C:\it3038c-scripts\python\doggo_FLIP_LEFT_RIGHT.jpg")    




