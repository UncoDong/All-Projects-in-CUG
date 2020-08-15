import cv2
import os
from math import *
import numpy as np

def tailor():# 裁剪图片
    images='./image/'
    if not os.path.exists(images):
            os.mkdir(images)
    img = cv2.imread("./imagess/"+fname)
    #print(img.shape)
    cropped = img[0:480, 110:410]  # 原点是左上角，裁剪坐标为[y0:y1, x0:x1]
    #cv2.imwrite(images+fname, cropped)
    return cropped

def revolve(img,fname):# 旋转图片
    #img = cv2.imread("./images-caijian/2019-12-12 10-09-50-316.jpg")
    height,width=img.shape[:2]
    degree=-90
    #旋转后的尺寸
    heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree)))) # 这个公式参考之前内容
    widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))
     
    matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)
     
    matRotation[0,2] +=(widthNew-width)/2  # 因为旋转之后,坐标系原点是新图像的左上角,所以需要根据原图做转化
    matRotation[1,2] +=(heightNew-height)/2  
     
    imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))

    cv2.imwrite('./image/'+fname,imgRotation)
    #cv2.imshow("img",img)# 显示原图片
    #cv2.imshow("imgRotation",imgRotation)# 显示旋转后的图片
    cv2.waitKey(0)

def rotate(frame,fname):
    frame1=np.rot90(np.rot90(np.rot90(frame)))
    cv2.imwrite('./image/'+fname,frame1)
    
if __name__=="__main__":
    all_files=os.listdir(os.curdir+'/imagess')#当前目录中的文件名用列表存储
    print(all_files[:4])
    for fname in all_files:
        img=tailor()
        #revolve(img,fname)
        rotate(img,fname)
