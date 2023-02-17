from skimage import data, filters
from skimage.viewer import ImageViewer
import scipy
from scipy import ndimage
import numpy as np
import PyQt5
import sklearn
from PIL import Image
from skimage import data
from skimage.color import rgb2gray
from skimage.viewer import ImageViewer
from skimage import io, color, data
import matplotlib.pyplot as plt
from skimage import feature

def opdracht1():
    #foto uitladen
    image = data.camera()

    image = filters.gaussian(image, 0.1, channel_axis=True)

    fig, ax = plt.subplots(3, 2, figsize=(8, 4))

    #original foto laten zien
    ax[0,0].imshow(image)
    ax[0,0].set_title("Original image")
    

    #masks
    maskblur=[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]] #blur

    mask1_x=[[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    mask1_y=[[1, 1, 1], [0, 0, 0],[-1, -1, -1]]

    mask2_y=[[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]
    mask2_x=[[1, 2, 1],[0, 0, 0],[-1, -2, -1]]

    mask3_y=[[0, 1, 1],[-1, 0, 1],[-1, -1, 0]]
    mask3_x=[[-1, -1, 0],[-1, 0, 1],[0, 1, 1]]



    image1_1 = scipy.ndimage.convolve(image, mask1_x)
    image1_2 = scipy.ndimage.convolve(image, mask1_y)

    image2_1 = scipy.ndimage.convolve(image, mask2_x)
    image2_2 = scipy.ndimage.convolve(image, mask2_y)

    image3_1 = scipy.ndimage.convolve(image, mask1_x)
    image3_2 = scipy.ndimage.convolve(image, mask1_y)
    


    optie1 = np.sqrt(np.square(image1_1) + np.square(image1_2))
    optie1 *= 255.0 / optie1.max()

    optie2 = np.sqrt(np.square(image2_1) + np.square(image2_2))
    optie2 *= 255.0 / optie2.max()

    optie3 = np.sqrt(np.square(image3_1) + np.square(image3_2))
    optie3 *= 255.0 / optie3.max()

    

 

    #masked images laten zien
    ax[0,1].imshow(optie1)
    ax[0,1].set_title("mask 1")

    ax[1,0].imshow(optie2)
    ax[1,0].set_title("mask 2")

    ax[1,1].imshow(optie3)
    ax[1,1].set_title("mask 3")

   
    plt.show()

def opdracht2():
    #foto uitladen
    image = data.camera()
    fig, ax = plt.subplots(3, 2, figsize=(8, 4))

    #original foto laten zien
    ax[0,0].imshow(image)
    ax[0,0].set_title("Original image")

    farid =filters.farid(image)
    prewitt = filters.prewitt(image)
    roberts = filters.roberts(image)

    #masked images laten zien
    ax[0,1].imshow(farid)
    ax[0,1].set_title("Farid")

    ax[1,0].imshow(prewitt)
    ax[1,0].set_title("laplace")

    ax[1,1].imshow(roberts)
    ax[1,1].set_title("roberts")

    plt.show()


def opdracht3():
    image = data.camera()
    fig, ax = plt.subplots(3, 2, figsize=(8, 4))

    #original foto laten zien
    ax[0,0].imshow(image)
    ax[0,0].set_title("Original image")

    edges1 = feature.canny(image, sigma=1)
    edges2 = feature.canny(image, sigma=2)
    edges3 = feature.canny(image, sigma=3)

    #masked images laten zien
    ax[0,1].imshow(edges1)
    ax[0,1].set_title("Canny sigma 1")

    ax[1,0].imshow(edges2)
    ax[1,0].set_title("Canny sigma 2")

    ax[1,1].imshow(edges2)
    ax[1,1].set_title("Canny sigma 3")
    
    plt.show()

opdracht1()

#hij maakt de afbeelding blauw/wit, maakt het minder ruizig