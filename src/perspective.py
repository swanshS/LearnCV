import cv2
import numpy as np
cv2.namedWindow('ori',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)
img=cv2.imread('Pic/pic2.jpeg')
h,w,c=img.shape
src=np.float32([[88,66],[186,90],[5,208],[150,257]])
dst=np.float32([[0,0],[240,0],[0,320],[240,320]])
m=cv2.getPerspectiveTransform(src,dst)
new=cv2.warpPerspective(img,m,(240,320))
while True:
    cv2.imshow('ori',img)
    cv2.imshow('new',new)
    key=cv2.waitKey(0)&0xff
    if key==ord('q'):
        break

cv2.destroyAllWindows()