import cv2
import numpy as np

cv2.namedWindow("origin1", cv2.WINDOW_NORMAL)
cv2.namedWindow("origin2", cv2.WINDOW_NORMAL)
cv2.namedWindow("add", cv2.WINDOW_NORMAL)
o1 = cv2.imread("./Pic/Pic.png")
if o1 is None:
    print("o1 is none")
else:
    o2 = np.full((847, 1275, 3), 155, np.uint8)
    print(o1.shape)
    while True:
        add = cv2.add(o1, o2)
        cv2.imshow(winname="origin1", mat=o1)
        cv2.imshow("origin2", o2)
        cv2.imshow("add", add)
        key = cv2.waitKey(0)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
