import cv2

cv2.namedWindow("ori", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("new", cv2.WINDOW_AUTOSIZE)

img = cv2.imread("Pic/Camera0.png")
print(img)
lap = cv2.Laplacian(img, -1, ksize=3)
cv2.imwrite("Pic/pic3.png", lap)
while True:
    cv2.imshow("ori", img)
    cv2.imshow("new", lap)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
