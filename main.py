import cv2
import numpy as np
import os

#resize size
dim=(1024,768)

#read images
readLeft=cv2.imread('lowHom1.png',cv2.IMREAD_COLOR)
readRight=cv2.imread('lowHom2.png',cv2.IMREAD_COLOR)

#for resizing if wanted.
Left=cv2.resize(readLeft,dim,interpolation = cv2.INTER_AREA)
Right=cv2.resize(readRight,dim,interpolation = cv2.INTER_AREA)

drawParams = dict(matchColor = (0,255,0), singlePointColor = None, flags = 2)

images=[]
images.append(readLeft)
images.append(readRight)


stitcher = cv2.Stitcher.create()
ret,pano = stitcher.stitch(images)


if ret==cv2.STITCHER_OK:
    print('panorama loading...')
    cv2.imshow('left',readLeft)
    cv2.imshow('right',readRight)
    cv2.imshow('Panorama',pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")
    print("images loaded but")

    if cv2.STITCHER_ERR_NEED_MORE_IMGS == 1:
        print('not enough keypoints to make pano')

    if cv2.STITCHER_ERR_HOMOGRAPHY_EST_FAIL == 2:
        print('RANSAC error')
    #print(cv2.STITCHER_ERR_NEED_MORE_IMGS)
    #print(cv2.STITCHER_ERR_HOMOGRAPHY_EST_FAIL)
    #print(cv2.STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL)
    print(ret)