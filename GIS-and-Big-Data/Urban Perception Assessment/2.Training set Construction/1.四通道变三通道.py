'''
功能：读取图片文件，得到对每张图片的数据矩阵
'''
# 读取图片的库
from PIL import Image
import os
import numpy as np


# 所有图片转换成RGB格式
def Photo2RGB(filpath):
      if os.path.exists('RGB/RGB_'+filpath[:-1]) == False:
            os.mkdir('RGB/RGB_'+filpath[:-1])
      manyfiles = os.listdir("img/"+filpath)
      for file in manyfiles:
            a = np.array(Image.open('img/'+filpath+file))
            print(a[0])
            print(a.shape)
            b = np.array(Image.open('img/'+filpath+file).convert('RGB'))
            print(b.shape)
            break
            image = Image.open('img/'+filpath+file).convert('RGB')
            image.save('RGB/RGB_'+filpath+file)
            

if __name__ == '__main__':
      # 文件路径
      
      filpaths = ["beautiful\\","boring\\","depressing\\","lively\\"]
      #filpaths = ["depressing\\","lively\\"]
      #filpaths = ["safety\\","wealthy\\"]
      filpaths = ["beautiful/"]
     
      # 遍历处理每个文件
      for filpath in filpaths:
            Photo2RGB(filpath)
            print("RGB"+filpath+'处理完毕')
                       
