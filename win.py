import cv2
import numpy as np
import matplotlib.pyplot as plt
cv2.namedWindow('new window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new window',640,480)
cv2.imshow('new window',0)
while True:
    key=cv2.waitKey(0)
    if (key==ord('q')):
        print("q pressed")
        break
print(key)
cv2.destroyAllWindows()