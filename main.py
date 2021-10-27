import cv2
import numpy as np
import os



#read images
readLeft=cv2.imread('lowHom1.png',cv2.IMREAD_COLOR)
readRight=cv2.imread('lowHom2.png',cv2.IMREAD_COLOR)

grayImgLeft = cv2.cvtColor(readLeft,cv2.COLOR_BGR2GRAY)
grayImgRight = cv2.cvtColor(readRight,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(grayImgLeft,None)
kp2, des2 = sift.detectAndCompute(grayImgRight,None)

match = cv2.BFMatcher()
matches = match.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.03*n.distance:
        good.append(m)



drawParams = dict(matchColor = (0,255,0), singlePointColor = None, flags = 2)

image3 = cv2.drawMatches(readLeft,kp1,readRight,kp2,good,None,**drawParams)

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
    cv2.imshow('key', image3)
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