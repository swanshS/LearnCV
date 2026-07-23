import cv2

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)

#写入视频编码格式
fourcc=cv2.VideoWriter.fourcc('M','J','P','G')

#获得为了视频打开摄像头，0是设备（摄像头）编号，CAP_ANY是为系统自动找到一个合适的API接口（哪一个底层的库来访问摄像头资源）
capture=cv2.VideoCapture(0,cv2.CAP_ANY)

#
vw=cv2.VideoWriter('Pic/MakeVideo.mp4',fourcc,25,(640,480),isColor=True)
#变量
a=0#保存图片数目
Camera_First=1#是否第一次获得摄像头资源
while capture.isOpened():#判断摄像头是否被打开
    #capture.read()两个返回值：第一个是是否成功读取帧，第二个是图片（mat格式u）
    ret,frame=capture.read()
    if ret==False:
        if Camera_First==1:
            print("Camera False!")
            Camera_First=0
    elif ret==True:
        if Camera_First==1:
            print("Camera OK!")
            Camera_First=0
            #显示图片
        cv2.imshow('video',frame)
        #保存到特定地址
        vw.write(frame)
        #等待key
        key=cv2.waitKey(1)
        #退出
        if key&0xFF==ord('q'):
            print("Quit the window!")
            break
        #保存
        elif key&0xFF==ord('s'):
            cv2.imwrite('Pic/Camera'+str(a)+'.png',frame)
            print("Picture Saved!")
            a=a+1

#释放资源
capture.release()
vw.release()
cv2.destroyAllWindows()