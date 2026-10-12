import cv2

image = cv2.imread("./Pic/Camera0.png")
if image is None:
    print("ream iamge fail")
    cv2.namedWindow("win", cv2.WINDOW_AUTOSIZE)

else:
    while True:
        cv2.imshow("win", image)
        key = cv2.waitKey(0)
        if key is ord("q"):
            break
    cv2.destroyAllWindows()
