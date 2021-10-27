import cv2


#foo = cv2.imread()
#bar = cv2.imread()
images1 = []
images1.append(foo)
images1.append(bar)
stitcher = cv2.Stitcher.create()
result = stitcher.stitch(images1)

cv2.imshow("result.jpg", result)
cv2.waitKey()