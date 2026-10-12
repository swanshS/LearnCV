import cv2
import numpy as np

cv2.namedWindow("text", cv2.WINDOW_NORMAL)
img = np.full((480, 640), 255, np.uint8)
while True:
    cv2.putText(img, "Hello World", (100, 20),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0))
    cv2.imshow("text", img)
    key = cv2.waitKey(0)
    if key == ord("q"):
        break
cv2.destroyAllWindows()
