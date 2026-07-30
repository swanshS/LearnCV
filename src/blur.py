import cv2
import numpy as np

cv2.namedWindow('ori',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)

img=cv2.imread('Pic/Pic.png')

kernel=np.ones((5,5),dtype=np.float32)/25

#new=cv2.blur(img,(5,5))
new=cv2.filter2D(img,-1,kernel)
while True:
    cv2.imshow('ori',img)
    cv2.imshow('new',new)
    key=cv2.waitKey(0)&0xff
    if key==ord('q'):
        break
cv2.destroyAllWindows()