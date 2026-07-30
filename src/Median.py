import cv2
import numpy as np

cv2.namedWindow('ori',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)

img=cv2.imread('Pic/Pic.png')
new=cv2.medianBlur(img,5)

while True:
    cv2.imshow('ori',img)
    cv2.imshow('new',new)
    key=cv2.waitKey(0)&0xff
    if key==ord('q'):
        break

cv2.destroyAllWindows()
