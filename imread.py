import cv2
cv2.namedWindow('WindowsForImages',cv2.WINDOW_NORMAL)
img=cv2.imread('/home/song/图片/壁纸2.jpeg',cv2.IMREAD_COLOR)
cv2.imshow('WindowsForImages',img)
while True:
    key=cv2.waitKey(0)
    if key==ord("q"):
        print("P Pressed!")
        break
cv2.destroyWindow('WindowsForImages')