# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Accessing and Modifying pixel values
# load a color image first
img = cv2.imread('messi5.jpg', cv2.IMREAD_COLOR )
cv2.imshow('image1',img)
plt.imshow(img)
# access a pixel value by its row and column coordinates
px = img[100,100]   # Show [157 166 200]
print(px) 

# accessing only blue pixel
blue = img[100,100,0]
print(blue) # Show 157 166 200

#  modify the pixel values the same way.
img[100,100] = [255,255,255]
print( img[100,100] ) # Show [255 255 255]

# Accessing Image Properties
print(img.shape) # number of rows, columns and channels (if color)
print(img.size) # Total number of pixels 
print(img.dtype) # Image datatype

# Image ROI
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# splitting and Merging Image Channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
b = img[:,:,0]
img[:,:,2] = 0
