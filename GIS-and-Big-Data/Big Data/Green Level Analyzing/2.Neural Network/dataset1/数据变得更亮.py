import cv2
import os
import numpy as np
import random
from skimage import color, exposure

# 所有暗色的图都变成亮的
def DARK2BRIGHT(filpath):
      manyfiles = os.listdir(filpath)
      for file in manyfiles:
            
            seg = cv2.imread(filpath+file)
            eqaimg = color.rgb2hsv(cv2.cvtColor(seg, cv2.COLOR_BGR2RGB))
            eqaimg[:, :, 2] = exposure.equalize_hist(eqaimg[:, :, 2])
            eqaimg = color.hsv2rgb(eqaimg)
            
            cv2.imwrite(filpath[:-1]+"_bright/"+file[:-3]+"jpg",
                        cv2.cvtColor((eqaimg *255.).astype(np.uint8),cv2.COLOR_RGB2BGR),
                        [int(cv2.IMWRITE_JPEG_QUALITY),95])
            

if __name__ == '__main__':

      filpaths = ["images_prepped_train/","images_prepped_test/"]
     
      # 遍历处理每个文件
      for filpath in filpaths:
            DARK2BRIGHT(filpath)
           
