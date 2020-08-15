import cv2
import os
import numpy as np
import random
# 一共11类物体
n_classes = 11
# 设置每次都相同的对应颜色
random.seed(1)
colors = [(random.randint(0, 255),
           random.randint(0, 255),
           random.randint(0, 255))
           for _ in range(n_classes)]

# 所有标签图象变成色图
def BLACK2COLOR(filpath):
      manyfiles = os.listdir(filpath)
      for file in manyfiles:
            seg = cv2.imread(filpath+file)
            seg_img = np.zeros_like(seg)
            for c in range(n_classes):
                  seg_img[:, :, 0] += ((seg[:, :, 0] == c) *
                                 (colors[c][0])).astype('uint8')
                  seg_img[:, :, 1] += ((seg[:, :, 0] == c) *
                                 (colors[c][1])).astype('uint8')
                  seg_img[:, :, 2] += ((seg[:, :, 0] == c) *
                                 (colors[c][2])).astype('uint8')
            cv2.imwrite(filpath[:-1]+"_color/"+file[:-3]+"jpg",seg_img,[int(cv2.IMWRITE_JPEG_QUALITY),95])

if __name__ == '__main__':

      filpaths = ["annotations_prepped_train/","annotations_prepped_test/"]
     
      # 遍历处理每个文件
      for filpath in filpaths:
            BLACK2COLOR(filpath)
           
