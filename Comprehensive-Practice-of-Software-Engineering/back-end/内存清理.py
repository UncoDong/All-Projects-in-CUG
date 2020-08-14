import os
import shutil
def eachFile(filepath):
    fileNames = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for file in fileNames:
        newDir = filepath + '/' + file # 将文件命加入到当前文件路径后面
        # print(newDir)
        # if os.path.isdir(newDir): # 如果是文件夹
        if os.path.isfile(newDir):  # 如果是文件
            end = os.path.splitext(newDir)[1]
            #print(end)
            if end!='.js' and end!='.css':
                if  end == ".xml" or '-' in file or end == ".wav" or end == ".mid": 
                    os.remove(newDir)
                    #print(newDir)
        else:
            if file == '__pycache__' or file == '.idea':
                shutil.rmtree(newDir)
                #print(newDir)
            else:
                eachFile(newDir)                #如果不是文件，递归这个文件夹的路径
eachFile('MusicBackEnd')
