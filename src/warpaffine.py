import cv2
import numpy as np
img=cv2.imread('Pic/Pic.png')
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('para',cv2.WINDOW_AUTOSIZE)
matrix=np.float32([[1,0,500],[0,1,300]])
h,w,c=img.shape
new=cv2.warpAffine(img,matrix,(w-150,h-200))
while True:
    cv2.imshow('img',img)
    cv2.imshow('para',new)
    key=cv2.waitKey(0)&0xff
    if key ==ord('q'):
        break
cv2.destroyAllWindows()
print(img.shape)
print(new.shape)