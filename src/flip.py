import cv2
import numpy as np

ori=cv2.imread('Pic/Pic.png')
cv2.namedWindow('origen',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('flip',cv2.WINDOW_AUTOSIZE)
flip=cv2.flip(ori,0)
while True:
    cv2.imshow('origin',ori)
    cv2.imshow('flip',flip)
    key=cv2.waitKey(0)&0xff
    if key == ord('q'):
        break
cv2.destroyAllWindows()