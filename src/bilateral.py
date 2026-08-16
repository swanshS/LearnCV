import cv2

cv2.namedWindow("ori", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("new", cv2.WINDOW_AUTOSIZE)

img = cv2.imread("Pic/Pic.png")
new = cv2.bilateralFilter(img, 10, 20, 30)

while True:
    cv2.imshow("ori", img)
    cv2.imshow("new", new)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
