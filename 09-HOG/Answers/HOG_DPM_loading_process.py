#!/usr/bin/env python ## #!/usr/local/bin/ python
#HOG_DPM_loading_process.py

#20180406: Test to uploading python 2.6 files
"""
2018 Ninth Laboratory, WorkShop - Lab 9. Computer Vision - Uniandes. 

Students:
Carlos Andrés Rivera Morales
Gabriel Andrés Espinosa Barrios

Background Student:
GAEB(Gabriel Andrés Espinosa Barrios)
Returning/re-entry Engineering PhD Graduate Student. Cod:200311728 Id:110279864X. 
University of the Andes(Universidad de los Andes). Bogota(Bogotá) D.C., Colombia.

Gabe Espinosa codes for Python
email: gabrielespinosa@gmail.com ; g-espino@uniandes.edu.co
Ph.D. Student. Returning/re-entry.
University of los Andes (Universidad de los Andes). Bogota D.C., Colombia.    
"""

import numpy as np
import pylab as plt
import dicom as dcm
import skimage.filter as filt
import glob as glob
from pyvtk2 import *

def DICOMreadImages():
    """
    Reads in all the DICOM images in a directory and assembles them
    into a single numpy volume. Assumes files are sequentially
    numbered. files types *dcm. Files "number".dcm; example 0388.dcm.
    """
   datafiles = glob.glob("./DICOM/*.dcm")
    vol = None
    for fname in datafiles:
        ds = dcm.read_file(fname)
        num = int(fname.split('.')[1].split("-")[-1])
        I = ds.pixel_array
        if vol == None:
            vol = np.zeros((I.shape[0],I.shape[1],len(datafiles)))
        vol[:,:,num-1] = I
    return vol

DICOMreadImages():


