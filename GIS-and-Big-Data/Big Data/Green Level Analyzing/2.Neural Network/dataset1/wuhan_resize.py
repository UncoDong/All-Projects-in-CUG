
from PIL import Image
import os
import numpy as np
# 所有图片转换成RGB格式
def PNG2JPG(filpath):
      manyfiles = os.listdir(filpath)
      
      for file in manyfiles:
            if os.path.exists(filpath[:-1]+"_resize/"+file[:-3]+"jpg") == False:
                  try:
                        image = Image.open(filpath+file)
                        image = image.resize((320, 320))
                        image = image.convert('RGB')
                        image.save(filpath[:-1]+"_resize/"+file[:-3]+"jpg",quality=95)
                  except:
                        ''''''      

if __name__ == '__main__':

      filpaths = ["hello2/"]
     
      # 遍历处理每个文件
      for filpath in filpaths:
            PNG2JPG(filpath)
            print(filpath+'resize完成')
      
