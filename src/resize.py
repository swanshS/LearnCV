import cv2
import numpy as np
ori=cv2.imread('Pic/Pic.png')
new=cv2.resize(ori,dsize=None,fx=0.5,fy=0.5)
cv2.namedWindow('origin',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)
while True:
    cv2.imshow('origin',ori)
    cv2.imshow('new',new)
    key = cv2.waitKey(0)&0xff
    if key == ord('q'):
        break
cv2.destroyAllWindows()