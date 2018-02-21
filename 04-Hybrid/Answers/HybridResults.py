#!/usr/bin/env python

#20180220: Uploading the Hybrid Answers Results
"""
Fourd Laboratory - Lab 4. Computer Vision - Uniandes. 
Students:
Carlos Andrés Rivera Morales
Gabriel Andrés Espinosa Barrios    
"""
#20180220: Lab4 answers
from skimage.data import coins, coffee, astronaut, clock, horse
import skimage
import matplotlib.pyplot as plt
from skimage import img_as_ubyte
from skimage import transform
from scipy import misc
import cv2

#IMAGES:
# Url images: 
#1. sucre 428.jpg=20180215img1.png (https://lh3.googleusercontent.com/-dPxKZJTpw1Y/Wnd754uYj4I/AAAAAAAAW3Q/3HJ1meCppuMneEyiCLYQGS0PSj4m2ghGgCJoC/w530-h707-n-rw/sucre%2B428.jpg)
#2. Abuelos.jpg-Bisabuelit@sMimamiNanita.jpg=20180215img2.png (https://lh3.googleusercontent.com/-IqJPZYrEKbg/WkGKiVc5T2I/AAAAAAAAWt0/oAT9VJHoOCYIs2xS-LLXzfGhJlZPbBKsACJoC/w530-h339-n-rw/Bisabuelit%2540sMimamiNanita.jpg)

#commands to import a image from a url:
#python 3.x:
#from PIL import Image
#import requests
#from io import BytesIO
#response = requests.get(url)
#img = Image.open(BytesIO(response.content))

#python 2.x:
#import urllib, cStringIO
#file = cStringIO.StringIO(urllib.urlopen(URL).read())
#img = Image.open(file)
#When cutting the image settings to the same pixels size 800X700 .png

face1 = misc.imread("/home/nbuser/library/ComputerVisionUniandes2/IBIO4680/04-Hybrid/Answers/imgs/20180215img1.png)
Andres = transform.resize(face1, (256,256))
face2 = misc.imread("/home/nbuser/library/ComputerVisionUniandes2/IBIO4680/04-Hybrid/Answers/imgs/20180215img2.png)
Antonio = transform.resize(face2, (256,256))

                    
#Filters
filtered_img = skimage.filters.gaussian(Andres, sigma=2, multichannel=True)
AndresO = img_as_ubyte(Andres)
AndresF = img_as_ubyte(filtered_img)
AntonioO = img_as_ubyte(Antonio)
AntonioF = skimage.filters.gaussian(AntonioO, sigma=5, multichannel=True)
AntonioF = img_as_ubyte(AntonioF)
newImage = cv2.subtract(AndresO,AndresF)
newImage = cv2.cvtColor(newImage, cv2.COLOR_RGB2GRAY)

resul[:,:,0] = resul[:,:,0]+newImage
resul[:,:,1] = resul[:,:,1]+newImage
resul[:,:,2] = resul[:,:,2]+newImage
#resul[0] = cv2.add(newImage, AntonioF[0])
#resul[1] = cv2.add(newImage, AntonioF[1])
#resul[2] = cv2.add(newImage, AntonioF[2])
plt.subplot(221)
plt.imshow(filtered_img)
plt.subplot(222)
plt.imshow(AntonioO)
plt.subplot(223)
plt.imshow(newImage)
plt.subplot(224)
plt.imshow(result)
