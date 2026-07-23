import cv2
import numpy as np
def Mouse(event,x,y,flags,N):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Left Button Pressed!")
    elif event==cv2.EVENT_RBUTTONDOWN:
        print("Right Button Pressed!")
    elif event==cv2.EVENT_LBUTTONUP:
            print("Left Button Released!")
    elif event==cv2.EVENT_RBUTTONUP:
            print("Right Button Released!")
cv2.namedWindow('window',cv2.WINDOW_GUI_EXPANDED)
cv2.resizeWindow('window',640,480)
img=np.zeros((480,640,3),dtype=np.uint8)
cv2.setMouseCallback('window',Mouse,param=None)
while True:
    cv2.imshow('window',img)
    key=cv2.waitKey(0)
    if key==ord('q'):
        break
cv2.destroyAllWindows()