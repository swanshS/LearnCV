import cv2
import numpy as np

np.random.seed(0)  # 固定随机种子，保证每次演示的噪声点一样

# =========================================================
# 演示1：合成一张带椒盐噪声的矩形二值图，看腐蚀/膨胀/开/闭的效果
# =========================================================
img = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(img, (50, 40), (150, 160), 255, -1)   # 白色矩形（前景）

# 前景外面加孤立小白点（模拟椒盐噪声）
for _ in range(30):
    x, y = np.random.randint(0, 200, 2)
    img[y, x] = 255
# 矩形内部加小黑点（模拟空洞）
for _ in range(15):
    x, y = np.random.randint(52, 148, 2)
    img[y, x] = 0

# 结构元素：5x5 矩形核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

eroded  = cv2.erode(img, kernel, iterations=1)      # 腐蚀：磨掉白噪点，矩形瘦一圈
dilated = cv2.dilate(img, kernel, iterations=1)     # 膨胀：填掉黑洞，矩形胖一圈（噪声点也放大）
opened  = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)   # 开运算：先腐蚀后膨胀，去噪、主体大小不变
closed  = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  # 闭运算：先膨胀后腐蚀，填洞、主体大小不变
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # 梯度：膨胀-腐蚀，得到轮廓

demo1 = np.hstack([img, eroded, dilated, opened, closed, gradient])
cv2.namedWindow('demo1: ori|erode|dilate|open|close|gradient', cv2.WINDOW_NORMAL)
cv2.resizeWindow('demo1: ori|erode|dilate|open|close|gradient', 1200, 200)
cv2.imshow('demo1: ori|erode|dilate|open|close|gradient', demo1)

# =========================================================
# 演示2：真实图片 转灰度 -> 二值化 -> 腐蚀/膨胀
# =========================================================
photo = cv2.imread('Pic/Camera0.png')
gray  = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
ret, bin_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 127 是阈值，255 是最大值

eroded2  = cv2.erode(bin_img, kernel, iterations=1)
dilated2 = cv2.dilate(bin_img, kernel, iterations=1)

demo2 = np.hstack([photo, cv2.cvtColor(bin_img, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(eroded2, cv2.COLOR_GRAY2BGR),
                   cv2.cvtColor(dilated2, cv2.COLOR_GRAY2BGR)])
cv2.namedWindow('demo2: ori|binary|erode|dilate', cv2.WINDOW_NORMAL)
cv2.resizeWindow('demo2: ori|binary|erode|dilate', 1280, 240)
cv2.imshow('demo2: ori|binary|erode|dilate', demo2)

while True:
    key = cv2.waitKey(0) & 0xff
    if key == ord('q'):
        break

cv2.destroyAllWindows()
