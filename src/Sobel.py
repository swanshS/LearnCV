import cv2
import numpy as np

cv2.namedWindow("ori", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("new", cv2.WINDOW_AUTOSIZE)

img = cv2.imread("Pic/Pic.png")  # uint 8
x = Sob = cv2.Sobel(img, -1, 1, 0, ksize=-1)
y = Sob = cv2.Sobel(img, -1, 0, 1, ksize=-1)
dst = cv2.add(x, y)

while True:
    cv2.imshow("ori", img)
    cv2.imshow("new", dst)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
