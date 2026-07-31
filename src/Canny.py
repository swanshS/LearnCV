import cv2
import numpy as np

cv2.namedWindow('ori',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)

img=cv2.imread('Pic/Camera0.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
can=cv2.Canny(gray,90,150)

while True:
    cv2.imshow('ori',img)
    cv2.imshow('new',can)
    key=cv2.waitKey(0)&0xff
    if key==ord('q'):
        break

cv2.destroyAllWindows()