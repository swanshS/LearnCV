import cv2
import numpy as np
import math
img=cv2.imread('Pic/Pic.png')
cv2.namedWindow('win',cv2.WINDOW_NORMAL)
src=np.float32([[0,0],[0,1],[1,0]])
dst=np.float32([[0,0],[1,0],[0,1]])
m=cv2.getAffineTransform(src,dst)
h,w,c=img.shape
new=cv2.warpAffine(img,m,(w,h))
while True:
    cv2.imshow('win',new)
    key=cv2.waitKey(0)&0xff
    if key == ord('q'):
        break
cv2.destroyAllWindows()