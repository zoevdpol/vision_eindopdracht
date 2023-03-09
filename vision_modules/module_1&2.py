import numpy as np
import matplotlib.pyplot as plt
import PyQt5
import sklearn
from PIL import Image
from skimage import data
from skimage.color import rgb2gray
from skimage.viewer import ImageViewer
from skimage import io, color, data
import matplotlib.pyplot as plt



#function that isolates the color red, function requires an image as a parameter
def IsolatorRed(image):

    #foto omzetten naar HSV
    HSV_pic = color.rgb2hsv(image)

    #orginele foto laten zien
    ax[0,0].imshow(color.hsv2rgb(HSV_pic))
    ax[0,0].set_title("Original")

    #histogram van original laten zien
    plt.title('Histogram of Hue org')
    plt.xlabel('Hue')
    plt.ylabel('Pixel amount')
    ax[1,0].hist(HSV_pic.flatten(), bins=256, facecolor='b' )

    #saturation per pixel omlaag gooien als het niet rood is
    low = 15 / 360 
    high = 245 / 360
    for i, row in enumerate(HSV_pic):
        for j, pixel in enumerate(row):
            #kijkt als iets grijs moet worden
            if  pixel[0] > low and pixel[0] < high: 
                #maakt het grijs door de saturation omlaag te doen
                HSV_pic[i][j][1] = 0 

    #foto isolated laten zien
    ax[0,1].imshow(color.hsv2rgb(HSV_pic), cmap=plt.cm.gray)
    ax[0,1].set_title("Isolated")

    #histogram isolated laten zien
    plt.title('Histogram of Hue iso')
    plt.xlabel('Hue')
    plt.ylabel('Pixel amount')
    ax[1,1].hist(color.hsv2rgb(HSV_pic).flatten(), bins=256, facecolor='g' )

       
#foto uitladen
original = io.imread("clown.jpg")
fig, ax = plt.subplots(2, 2, figsize=(8, 4))
IsolatorRed(original)
#laten zien
plt.show()
