import numpy as np
import cv2
color = 255
img = np.full((480,640),color,np.uint8)
cv2.namedWindow('NumpyWindow',cv2.WINDOW_AUTOSIZE)

def OnMouse(event,x,y,flag,para):
    global color
    #左键：亮度升高
    if event==cv2.EVENT_LBUTTONDOWN:
        color=(color+50+255)%255
    #右键：亮度降低
    elif event==cv2.EVENT_RBUTTONDOWN:
        color=(color+255-50)%255
    img = np.full((480,640),color,np.uint8)
    cv2.imshow('NumpyWindow',img)
cv2.setMouseCallback('NumpyWindow',OnMouse,param=None)
while True:
    cv2.imshow("NumpyWindow",img)
    key =cv2.waitKey(0)
    img = np.full((480,640),color,np.uint8)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
