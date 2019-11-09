# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import obrazy
import test

from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


def createFundusMask(inputImage):
        x, y, channels =inputImage.shape
        print(str(x)+" "+str(y))
        x = int(x/2)
        y = int(y/2)
        radius=x
        fundusMask=inputImage
        _, fundusMask=cv2.threshold(fundusMask,0,0,cv2.THRESH_BINARY_INV)
        fundusMask=cv2.circle(fundusMask,(y,x),radius,(255,255,255),-1)
        plt.imshow(fundusMask)
        plt.show()
        return fundusMask


        # plt.imshow(self.inputImage[:,:,1],cmap='binary')
        #Tato moznost mi pride lepsia z dovodu ze su lepsie rozoznatelne zily na nej
        #plt.imshow(self.inputImage[:, :, 0])
        
  



inputImage = cv2.imread('test2.TIF')


#creating mask/fundus
img=createFundusMask(inputImage)


