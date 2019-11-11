# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy.misc

import cv2
import obrazy
import test
import numpy
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import morphology
from skimage import color
from skimage.filters import threshold_otsu


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
fundus_mask=createFundusMask(inputImage)


#elementarne prvky
se=morphology.octagon(9,8)

se1=morphology.disk(5)
se1=numpy.delete(se1, 0, 0)
se1=numpy.delete(se1, 9, 0)
se1=numpy.delete(se1, 0, 1)
se1=numpy.delete(se1, 9, 1)

se2=morphology.disk(3)
se2=numpy.delete(se2, 0, 0)
se2=numpy.delete(se2, 5, 0)
se2=numpy.delete(se2, 0, 1)
se2=numpy.delete(se2, 5, 1)

se11=morphology.disk(6)
se11=numpy.delete(se11, 0, 0)
se11=numpy.delete(se11, 11, 0)
se11=numpy.delete(se11, 0, 1)
se11=numpy.delete(se11, 11, 1)

se22=morphology.disk(3)
se22=numpy.delete(se22, 0, 0)
se22=numpy.delete(se22, 5, 0)
se22=numpy.delete(se22, 0, 1)
se22=numpy.delete(se22, 5, 1)

#Prva vetva

#Morfologicke otvorenie

i=inputImage[:,:,1] #vyberieme greenpicture
i = color.rgb2gray(i)

Img1=morphology.opening(i,se2)
plt.imshow(Img1,cmap=plt.cm.gray)
plt.show()

Img1=morphology.reconstruction(Img1, i)
plt.imshow(Img1,cmap=plt.cm.gray)
plt.show()


Img1=Img1-morphology.black_tophat(Img1,se1 )-morphology.white_tophat(Img1, se1) #subtract
plt.imshow(Img1,cmap=plt.cm.gray)
plt.show()

Img2=morphology.closing(Img1, se)
plt.imshow(Img2,cmap=plt.cm.gray)
plt.show()


Img2=Img2-Img1

fig = plt.figure () 
plt.imshow(Img2,cmap=plt.cm.gray)
plt.show()
#fig.savefig ( 'plot.png' )
level = threshold_otsu(Img2)
th, bw = cv2.threshold(Img2, level, 255, cv2.THRESH_BINARY);



bw=morphology.remove_small_objects(bw, 1500, 8) ## nefunguje opravit obrazok na black and white rucne


plt.imshow(bw,cmap=plt.cm.gray)
plt.show()






































