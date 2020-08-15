# -*- encoding: utf-8 -*-
import cv2
import os
import datetime


namelist=[]
def time_id (fname,start_time):#（csv文件名，开始时间），返回视频时间列表，单位：秒
    f=open(fname,'r')#（文本打开csv文件）
    idlist=[]
    start =datetime.datetime.strptime( start_time,'%Y-%m-%d %H:%M:%S:%f')#开始时间 datetime类型精确到毫秒
    print(start)
    print(type(start))
    next(f)#跳过csv文件第一行表头
    lines = f.readlines()#每一行存数据进lines[]里
    print(lines[3])
    for line in lines:
        str_ = line.split(',')[0]#str_是真实时间
        namelist.append(str_)
        #print(str_)
        d = datetime.datetime.strptime(str_,'%Y-%m-%d %H:%M:%S:%f')#把真实时间转化为datetime类型精确到毫秒
        delta = d-start#相减得到视频时间
        sec = delta.total_seconds()#将视频时间换成秒数
        idlist.append(sec)#把视频秒数存进idlist
    f.close()
    return idlist



def imagewrite(fname,idlist):#（mp4文件名，视频时间列表（单位：秒））
    
    images = './imagess/'
    if not os.path.exists(images):
        os.mkdir(images)          #如果当前目录没有/image/这个路径，就创建文件夹
        
    cap = cv2.VideoCapture(fname)  #打开视频文件
    fps = cap.get(cv2.CAP_PROP_FPS)#获取当前视频平均帧率
    fnum = cap.get(cv2.CAP_PROP_FRAME_COUNT)#获取当前视频总帧率
    str_=0
    for timeid in idlist:
        frame_id = int(timeid*fps) #秒数*平均帧率向下取整得到对应帧
        if(frame_id<=fnum):#如果得到的帧数小于总帧数就取出当前帧
            #print(frame_id)
            cap.set(cv2.CAP_PROP_POS_FRAMES,frame_id)#设置当前帧数为frame_id
            success,frame = cap.read()#read（）返回值为一个bool（是否读取成功）和一个视频帧
            if success:
                cv2.imwrite(images+namelist1[str_]+'.jpg',frame)#保存当前帧为图片
                print(namelist1[str_])
                str_=str_+1
            else:
                print("失败")
    cap.release()

timeidlist = time_id('VID_20191229_133445.mp4.csv','2019-12-29 13:34:45:594')
#print(timeidlist)
namelist1=[]
for each in namelist:
    a=each.replace(":", "-")
    namelist1.append(a)
print(type(namelist1[3]))
imagewrite( "VID_20191229_133445.mp4",timeidlist)   

##images = './image/'
##if not os.path.exists(images):
##    os.mkdir(images)
##
##f=open('VID_20191212_100933.mp4.csv','r')
##cap = cv2.VideoCapture("VID_20191212_100933.mp4")
##fps = cap.get(cv2.CAP_PROP_FPS)
##fnum = cap.get(cv2.CAP_PROP_FRAME_COUNT)
##print(fnum)
##print(fps)
##start =datetime.datetime.strptime( '2019-12-12 10:09:33:691','%Y-%m-%d %H:%M:%S:%f')
##next(f)
##lines = f.readlines()
##for line in lines:
##        str_ = line.split(',')[0]
##        d = datetime.datetime.strptime(str_,'%Y-%m-%d %H:%M:%S:%f')
##        delta = d-start
##        sec = delta.total_seconds()
##        frame_id = int(sec*fps)
##        if(frame_id<=fnum):
##            print(frame_id)
##            cap.set(cv2.CAP_PROP_POS_FRAMES,frame_id)
##            success,frame = cap.read()
##            if success:
##                cv2.imwrite(images+str(str_)+'.jpg',frame)
##            else:
##                print("失败")
##        print (sec)
##
##f.close()
##cap.release()


 

 
