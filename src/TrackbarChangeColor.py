import cv2
import numpy as np
def Callback(position):
    pass

cv2.namedWindow('window',cv2.WINDOW_NORMAL)
img=cv2.imread('./Pic/Pic.png')
cv2.createTrackbar('value','window',0,100,Callback)
while True:
    value=int(cv2.getTrackbarPos('value','window'))
    Val=np.full(img.shape,value,np.uint8)
    res=cv2.add(img,Val)
    cv2.imshow('window',res)
    key=cv2.waitKey(1)&0XFF
    if key==ord('q'):
        break
cv2.destroyAllWindows()