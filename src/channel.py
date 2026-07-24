import cv2
import numpy

img=cv2.imread('./Pic/Pic.png')
cv2.namedWindow('Pic',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Pic',480,640)
#分割通道
b,g,r=cv2.split(img)
while True:
    #合并通道
    cv2.imshow('Pic',cv2.merge((g,r,b)))
    key=cv2.waitKey(0)
    if key==ord('q'):
        break
cv2.destroyAllWindows()