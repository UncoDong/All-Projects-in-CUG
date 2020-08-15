import pandas as pd                         #导入pandas包
import numpy as np
import json

def Hot_json(emotion,name):
      
      data = pd.read_csv(emotion+"_Tran_"+name+"_data.csv")             #读取csv文件
      a = data.loc[:, ['Time','Latitude', 'Longitude',emotion]]       #打印行中特定列
      lists = a.values.tolist()


      # 存放坐标数据的列表
      inputlist = []
      for i in range(len(lists)):
            feature =  { "type": "Feature", "properties": {"time": lists[i][0],"mag": float(lists[i][3])},
                   "geometry": { "type": "Point",
                                 "coordinates": [float(lists[i][2]), float(lists[i][1]) ] } }
            
            inputlist.append(feature)
            
      inputjson = {"type": "FeatureCollection",
                   "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                   "features":inputlist}

      res2=json.dumps(inputjson, sort_keys=True, indent=4, separators=(',', ':'))
      with open(name+"_json/"+emotion+"_"+name+'_hot.json','w',encoding='utf-8') as f:#打开文件
          f.write(res2)#在文件里写入转成的json串

if __name__ == '__main__':
      emotions = ['beautiful','boring','depressing','lively','safety','wealthy']
      for emotion in emotions:
            Hot_json(emotion,"20191229")

