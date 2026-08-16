import cv2
import numpy as np

cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
img1 = np.zeros((480, 640), np.uint8)
img2 = np.zeros((480, 640), np.uint8)
img1[20:100, 20:100] = 255
img2[70:200, 70:200] = 255

img_and = cv2.bitwise_and(img1, img2)
img_not = cv2.bitwise_not(img1)
img_or = cv2.bitwise_or(img1, img2)
img_xor = cv2.bitwise_xor(img1, img2)
while True:
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)
    cv2.imshow("and", img_and)
    cv2.imshow("not", img_not)
    cv2.imshow("or", img_or)
    cv2.imshow("xor", img_xor)
    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
