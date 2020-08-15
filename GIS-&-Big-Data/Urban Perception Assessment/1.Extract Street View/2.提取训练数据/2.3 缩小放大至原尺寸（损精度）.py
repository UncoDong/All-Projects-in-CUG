import cv2
import os

lable=["beautiful","boring","depressing","lively","safety","wealthy"]

def resize(lable):# 翻转图片
    images='./'+lable+'_resize3/'
    if not os.path.exists(images):
            os.mkdir(images)
    img = cv2.imread("./"+lable+"/"+fname)

    height, width = img.shape[:2]
    reSize1 = cv2.resize(img, (int(width/3), int(height/3)), interpolation=cv2.INTER_CUBIC)
    reSize2 = cv2.resize(reSize1, (width, height), interpolation=cv2.INTER_CUBIC)
    

    cv2.cv2.imwrite(images+fname[:-4]+'_r3.jpg', reSize2)

    return reSize2

if __name__=="__main__":
    for l in lable:
        all_files=os.listdir(os.curdir+'/'+l)#当前目录中的文件名用列表存储
    
        for fname in all_files:
            #print(fname)
            img=resize(l)
