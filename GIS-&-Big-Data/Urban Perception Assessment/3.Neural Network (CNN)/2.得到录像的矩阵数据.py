'''
用来得到录像截图的矩阵数据
'''
from PIL import Image
import os
import pickle
import numpy as np

# 截图名字
imgname = []
# 截图数据
imgdata = []

# 得到截图数据
def Getimg(filpath):
      manyfiles = os.listdir(filpath)
      for file in manyfiles:
            img = np.array(Image.open(filpath+file))#读取图片
            imgname.append(file)
            imgdata.append(img)
      print('{}total imagenames : {:d}'.format(str(filpath), len(imgname)))
      print('{}total imagedatas : {:d}'.format(str(filpath), len(imgdata)))


if __name__ == "__main__":
      filpaths = ["camera_img2\\"]
      Getimg(filpaths[0])
      with open("video2.pickle","wb") as f:
            pickle.dump([imgname, imgdata],f)
