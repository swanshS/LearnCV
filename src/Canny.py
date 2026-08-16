import cv2
import numpy as np
import sys  # 导入 sys 模块，用于安全退出

cv2.namedWindow("ori", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("new", cv2.WINDOW_AUTOSIZE)

img = cv2.imread("Pic/Camera0.png")
if img is None:
    print("错误：无法加载图像，请检查路径 Pic/Camera0.png")
    sys.exit()  # 使用 sys.exit() 代替 exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
can = cv2.Canny(gray, 90, 150)

while True:
    cv2.imshow("ori", img)
    cv2.imshow("new", can)
    key = cv2.waitKey(1) & 0xFF  # 使用 waitKey(1) 避免阻塞
    if key == ord("q"):
        break
cv2.destroyAllWindows()
