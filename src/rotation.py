import cv2
import numpy as np
cv2.namedWindow('window',cv2.WINDOW_AUTOSIZE)
img=cv2.imread('Pic/Pic.png')
h,w,c=img.shape
m=cv2.getRotationMatrix2D((w/2,h/2),45,1.0)
print(m)
rot=cv2.warpAffine(img,m,(w,h))
while True:
    cv2.imshow('window',rot)
    key=cv2.waitKey(0)&0xff
    if key==ord('q'):
        break
cv2.destroyAllWindows()