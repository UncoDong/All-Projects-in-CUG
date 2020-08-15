import cv2
import os

lable = ["beautiful","boring","depressing","lively","safety","wealthy"]

def Flip( lable ):# 翻转图片
    images='./'+lable+'_fjpg/'
    if not os.path.exists(images):
            os.mkdir(images)
    img = cv2.imread('./'+lable+'/'+fname)

    img_ = cv2.flip(img,1,dst=None) #水平镜像
    img_ = cv2.flip(img_,1,dst=None) #水平镜像
    cv2.cv2.imwrite(images+fname[:-4]+'_f.jpg', img_)

    return img_

if __name__=="__main__":
    for l in lable:
        all_files=os.listdir(os.curdir+'/'+l)#当前目录中的文件名用列表存储
        print(all_files[:4])
        for fname in all_files:
            img=Flip(l)
