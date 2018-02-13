#!/usr/bin/env python


"""
Tercer laboratorio: 
    Gabriel Espinosa
    Carlos Rivera
"""
from glob import glob
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from skimage import transform
from urllib import urlretrieve
import os
import tarfile
import random
from skimage.io import imsave
import scipy.io as sio
import pickle
import time

mypath = '/tmp/gabrielcarloslab/BSR/BSDS500/data/images/train/'
mypathLabels = '/tmp/gabrielcarloslab/BSR/BSDS500/data/groundTruth/train/'
link = "http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz"
my_file = '/tmp/gabrielcarloslab/bsr500prueba50.tgz'
outputImagesDir = "/tmp/gabrielcarloslab/salImages/"

num_to_select = 7



def getFiles():
    
    imlist = []
    ImagesSall = []
    ImagesSallLabels = []

    if not os.path.exists("/tmp/gabrielcarloslab"):
        os.makedirs("/tmp/gabrielcarloslab")
    os.chdir('/tmp/gabrielcarloslab')
    
    if os.path.exists(my_file) == False:
        filename, headers = urlretrieve(link, my_file)
    
    if os.path.exists('/tmp/gabrielcarloslab/BSR') == False:
        tar = tarfile.open(my_file)
        tar.extractall()
        tar.close()
    
    tic = time.time()
        
    if not os.path.exists(outputImagesDir):
        os.makedirs(outputImagesDir)
    
    
    
    
    count = 0
    for each in glob(mypath + "*"):
        word = each.split("/")[-1].split(".")[0]
        if word == 'Thumbs':
            continue
        imlist.append(word)
        #print(word)
    list_of_random_items = random.sample(imlist, num_to_select)
    
    aaa=plt.figure()
    
    saltoGraphics = 0
    
    

    
    for ind in range(num_to_select):
        pathIm = ''.join([mypath,list_of_random_items[ind],".jpg" ])
        face = misc.imread(pathIm)
        face = transform.resize(face, (256,256))
        ImagesSall.append(face)
        imsave(''.join([outputImagesDir,list_of_random_items[ind],".jpg"]),face)
        plt.subplot2grid((num_to_select,9), (ind,0))
        plt.imshow(face)
        plt.axis('off')
        
        mat_contents = sio.loadmat(''.join([mypathLabels,list_of_random_items[ind],".mat"]))
        arrayImages=mat_contents['groundTruth']
        selecSegment=0
        selecSegmentAlt=0
        for i in range(1,9):
            if i%2 is not 0:
                plt.subplot2grid((num_to_select,9), (ind,i))
                myImageLabel = arrayImages[0][selecSegment][0][0][0]
                ImagesSallLabels.append( myImageLabel )
                plt.imshow(transform.resize(myImageLabel, (256,256)))               
                selecSegment=selecSegment+1
                plt.axis('off')
            else:
                plt.subplot2grid((num_to_select,9), (ind,i))
                myImageLabel = arrayImages[0][selecSegmentAlt][0][0][1]
                ImagesSallLabels.append( myImageLabel )
                plt.imshow(transform.resize( myImageLabel , (256,256)), cmap=plt.cm.gray)
                selecSegmentAlt=selecSegmentAlt+1
                plt.axis('off') 

        
    toc = time.time()
    
    datos={"original": ImagesSall, "labels":ImagesSallLabels}
    with open(''.join([outputImagesDir,'objectss.pkl']), 'w') as f:  # Python 3: open(..., 'wb')
        pickle.dump(datos, f)
    
    print (''.join(["\n Computation time = ",str(1000*(toc - tic)), "ms"]))
    aaa.suptitle(''.join(["BSDS500 Dataset \n Computation time = ",str(1000*(toc - tic)), "ms"]), fontsize="x-large")
    plt.show()
        
getFiles()
