import cv2
import numpy as np
def cb(x):
    pass
#创建窗口
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('window',640,480)

#创建trackbar
cv2.createTrackbar('R','window',0,255,cb)
cv2.createTrackbar('G','window',0,255,cb)
cv2.createTrackbar('B','window',0,255,cb)

#创建numpy的元素
img=np.zeros((480,640,3),dtype=np.uint8)

#显示窗口
while True:
    #获取trackbar的值
    r=cv2.getTrackbarPos('R','window')
    g=cv2.getTrackbarPos('G','window')
    b=cv2.getTrackbarPos('B','window')

    #赋值
    img[:,:]=[b,g,r]
    cv2.imshow('window',img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

#释放资源
cv2.destroyAllWindows()