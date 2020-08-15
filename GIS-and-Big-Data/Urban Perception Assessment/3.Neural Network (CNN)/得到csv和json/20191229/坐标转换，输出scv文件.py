'''
坐标转换，再次输出scv文件
'''

from math import *
pi = 3.14159265358979324
a = 6378245.0
ee = 0.00669342162296594323
#从纬度转换
def transformLat( x, y ):
      ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * sqrt(abs(x))
      ret += (20.0 * sin(6.0 * x * pi) + 20.0 * sin(2.0 * x * pi)) * 2.0 / 3.0
      ret += (20.0 * sin(y * pi) + 40.0 * sin(y / 3.0 * pi)) * 2.0 / 3.0
      ret += (160.0 * sin(y / 12.0 * pi) + 320 * sin(y * pi / 30.0)) * 2.0 / 3.0
      return ret

#从经度转换
def transformLon( x, y ):
      ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * sqrt(abs(x))
      ret += (20.0 * sin(6.0 * x * pi) + 20.0 * sin(2.0 * x * pi)) * 2.0 / 3.0
      ret += (20.0 * sin(x * pi) + 40.0 * sin(x / 3.0 * pi)) * 2.0 / 3.0
      ret += (150.0 * sin(x / 12.0 * pi) + 300.0 * sin(x / 30.0 * pi)) * 2.0 / 3.0
      return ret;


#WGS变成gcj
def wgs2gcj(wgLat, wgLon):
      dLat = transformLat(wgLon - 105.0, wgLat - 35.0)
      dLon = transformLon(wgLon - 105.0, wgLat - 35.0)
      radLat = wgLat / 180.0 * pi
      magic = sin(radLat)
      magic = 1 - ee * magic * magic
      sqrtMagic = sqrt(magic)
      dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * pi)
      dLon = (dLon * 180.0) / (a / sqrtMagic * cos(radLat) * pi)
      mgLat = wgLat + dLat
      mgLon = wgLon + dLon
      return str(mgLat),str(mgLon)

#GCJ变成WGS
def gcj2wgs( mglat, mglon):
      glat,glon = wgs2gcj(mglat, mglon)
      dlat = glat - mglat
      dlon = glon - mglon
      wglat = mglat - dlat
      wglon = mglon - dlon
      return wglat,wglon

import csv
import os

emotions = ['beautiful','boring','depressing','lively','safety','wealthy']

for emotion in emotions:
      # 设置输出文件
      out = open(emotion+"_Tran_20191229_data.csv","w")   

      #打开csv
      matedata_path = os.path.abspath(emotion+'_20191229_data.csv')
      if os.path.exists(matedata_path):
          with open(matedata_path, encoding='utf-8') as f:
              csv_reader_lines = csv.reader(f)
              # 遍历csv的每一行
              # 将每行的经纬度进行转换
              for one_line in csv_reader_lines:
                  try:
                        one_line[2],one_line[3] = wgs2gcj(float(one_line[2]),float(one_line[3]))
                  except:
                        print(one_line)
                  
                  output = ""
                  # 重新组合改行数据
                  for each in one_line:
                        output+=each
                        output+=","
                  # 写入文件
                  out.writelines(output)
                  out.write("\n")
      out.close()

                   
            
            
        



      
