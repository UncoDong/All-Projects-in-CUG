import zipfile
import os
def Zip(dirpath,outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath,'')

        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
    zip.close()
    print(dirpath+"处理完毕")
    
path = ["RGB_safety.zip","RGB_wealthy.zip"]
path2 = ["RGB_safety/","RGB_wealthy/"]

filpaths = ["beautiful","boring","depressing","lively"]

for i in range(4):
    Zip("RGB_"+filpaths[i]+"/","RGB_"+filpaths[i]+".zip")
