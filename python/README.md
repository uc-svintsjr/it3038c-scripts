# LAB 7
Before you can run these Python scripts, which use the plugin Pillow, you will need to install the plugin<br>    
For those who use Visual Studio Code, run this command in terminal<br>
`pip install pillow`<br>  
Now that you have the plugin installed. Find an image off the internet of your choice and download it to your hard drive.<br>  
#### Example 1) UnsharpMask  
 
Now, in Python run the following code:

```
from PIL import Image    
from PIL import ImageFilter       
from PIL.ImageFilter import (      
    UnsharpMask  
    )    
simg = Image.open('C:\it3038c-scripts\python\doggo.jpg')

dimg = simg.filter(UnsharpMask(radius=2, percent=150, threshold=3))
dimg.save("C:\it3038c-scripts\python\doggy.jpg") <br>  
```
The syntax above will open the picture you downloaded and then apply a filter using the ImageFilter module.<br>
Unsharp masking is an image sharpening technique. The Unsharp mask is then combined with the original positive image, creating an image that is less blurry than the original.  <br>  
#### Example 2) Split
Now, in Python run the following code:

```
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
```		
The syntax above will open the picture you downloaded and then split it into three different RGB pictures using the Image.split() method.
Once you run this code you will see three copies of the same image but in different RBG colors.
<br>  
#### Example 3) Transpose
Now, in Python run the following code:
```
from PIL import Image
#
img = Image.open('C:\it3038c-scripts\python\doggo.jpg')
img.transpose(Image.FLIP_LEFT_RIGHT).save(
    "C:\it3038c-scripts\python\doggo_FLIP_LEFT_RIGHT.jpg")    
``` 
The syntax above will open the picture you downloaded and then using the method Image.transpose which flips or rotates in 90 degree steps.
Here we use the FLIP_LIGHT_RIGHT direction which flips the image from left to right.
