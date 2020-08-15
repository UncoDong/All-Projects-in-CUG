import cv2
import os
import math
import numpy as np

def tailor():# 裁剪图片
    images='./images_resize/'
    if not os.path.exists(images):
            os.mkdir(images)
    img = cv2.imread("./images/"+fname)
    #print(img.shape)
##    x=480
##    y=300
##    m=x*0.9
##    n=y*0.9

##    cropped = img[0:int(n),0:int(m)]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
##    cv2.imwrite(images+fname[:-4]+'_1.jpg', cropped)
##    cropped = img[0:int(n),int(x-m):int(x)]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
##    cv2.imwrite(images+fname[:-4]+'_2.jpg', cropped)
##    cropped = img[int(y-n):int(y),0:int(m)]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
##    cv2.imwrite(images+fname[:-4]+'_3.jpg', cropped)
##    cropped = img[int(y-n):int(y),int(x-m):int(x)]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
##    cv2.imwrite(images+fname[:-4]+'_4.jpg', cropped)
##    cropped = img[int((y-n)/2):math.ceil((y+n)/2),int((x-m)/2):math.ceil((x+m)/2)]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
##    cv2.imwrite(images+fname[:-4]+'_5.jpg', cropped)

    cropped = img[146:446,0:480]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(images+fname[:-4]+'.jpg', cropped)


    return cropped


if __name__=="__main__":
    all_files=os.listdir(os.curdir+'/images')#当前目录中的文件名用列表存储
    print(all_files[:4])
    for fname in all_files:
        img=tailor()

