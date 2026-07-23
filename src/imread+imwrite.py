import cv2
cv2.namedWindow('WindowsForImages',cv2.WINDOW_NORMAL)
img=cv2.imread('/home/song/图片/壁纸2.jpeg',cv2.IMREAD_COLOR)
while True:
    cv2.imshow('WindowsForImages',img)
    key=cv2.waitKey(0)
    if key==ord("q"):
        print("P Pressed!")
        break
    elif key==ord('s'):
        cv2.imwrite('/home/song/Code/Python/CV/Pic.png',img)
        print("Picture has been saved!")
        break
cv2.destroyWindow('WindowsForImages')