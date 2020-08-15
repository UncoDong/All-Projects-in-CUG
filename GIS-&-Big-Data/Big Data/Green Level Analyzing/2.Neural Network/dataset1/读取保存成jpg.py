from PIL import Image
import os
import numpy as np

# 所有图片转换成RGB格式
def PNG2JPG(filpath):
      manyfiles = os.listdir(filpath)
      for file in manyfiles:
            image = Image.open(filpath+file)
            image.save(filpath[:-1]+"2/"+file[:-3]+"jpg",quality=95)

if __name__ == '__main__':

      filpaths = ["annotations_prepped_test/","images_prepped_test/"]
     
      # 遍历处理每个文件
      for filpath in filpaths:
            PNG2JPG(filpath)
           
