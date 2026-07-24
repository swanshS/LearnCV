import cv2
import numpy as np
cv2.namedWindow('DrawLine',cv2.WINDOW_NORMAL)
img=np.full((480,640,3),255,dtype=np.uint8)
cv2.resizeWindow('DrawLine',640,480)
#img,起始点，终止点，颜色，线的类型
cv2.line(img,(320,0),(0,480),(255,0,0),cv2.LINE_4)
while True:
    cv2.imshow('DrawLine',img)
    key=cv2.waitKey(0)
    if key==ord('q'):
        break
cv2.destroyAllWindows()