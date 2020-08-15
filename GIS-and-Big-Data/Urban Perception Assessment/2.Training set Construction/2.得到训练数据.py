'''
功能：读取图片文件，得到对每张图片的数据矩阵
'''

# 读取图片的库
from PIL import Image
import numpy as np
import os
import pickle

data = {}
# 图片转换成矩阵
def Img2array(filpath):
      # 每次清理数据
      data.clear()
      manyfiles = os.listdir(filpath)
      for file in manyfiles:
            img = np.array(Image.open(filpath+file))# 读取图片
            # 抹掉小数点后的后缀，作为key值
            mid = file.split('.')
            data[mid[0]+'.'+mid[1]+'.'+mid[2]] = img
      print('{}total images : {:d}'.format(str(filpath), len(data)))

def GetTrain(filname):
      # 打开数据集
      with open('csv_message\\'+filname+'_csv_message.pickle','rb') as f:
            csv = pickle.load(f)

      # 存放训练数据和训练标签的列表
      train_data = []
      train_labels = []
      # 通过key寻找相同名字的数据
      for key in sorted(data.keys()):    
            try:
                  train_labels.append(int(csv[key]))
                  train_data.append(data[key])
            except :
                  train_data.append(data[key])
                  train_labels.append(int(csv[key[:-3]]))
                  
      #数据都转换成np类型
      train_data = np.array(train_data)
      train_labels = np.array(train_labels)
      with open(filname+'_train_data.pickle','wb') as f:
                  pickle.dump([train_data, train_labels],f)
      print(filname+'训练数据处理完毕')
            
if __name__ == '__main__':
      # 保存文件的路径
      if os.path.exists('img_message') == False:
            os.mkdir('img_message')
      # 文件列表
      filpaths = ["beautiful\\","boring\\",\
                  "depressing\\","lively\\","safety\\","wealthy\\"]
      filpaths = ["beautiful\\","boring\\"]
      filpaths = ["depressing\\","lively\\"]
      
      for filpath in filpaths:
            Img2array("RGB/RGB_"+filpath)
            GetTrain(filpath[:-1])
            print(filpath+'保存完毕')
