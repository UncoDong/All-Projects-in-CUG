import os
import pickle
import numpy as np
import csv

from tensorflow.keras.models import model_from_json

# 加载模型
def Score(name,video):
      #model = keras.models.load_model('my_model.h5')
      # load json and create model
      json_file = open(name+'_model.json', 'r')
      loaded_model_json = json_file.read()
      json_file.close()
      model = model_from_json(loaded_model_json)
      model.load_weights(name+'_model.json.h5')
      model.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])
      print('读取模型完毕')
      # 得到截图数据
      with open("camera_data/"+video+".pickle","rb") as f:
            imgname,imgdata = pickle.load(f) 
      #将截图数据转换成np类型
      imgdata = np.array(imgdata,'float32')
      print(imgdata.dtype)
      print(imgdata.shape)
      imgdata/=255
      print('读取图像完毕')
      #开始预测
      prediction = model.predict(imgdata)
      print('预测完毕')

      #预测结果汇总
      scoredata = {}
      for i in range(len(imgname)):
            #print(mid)
            mid = imgname[i].split('.')
            try:
                  scoredata[mid[0]]+=prediction[i]
            except:
                  scoredata[mid[0]]=prediction[i]
      print(str(i)+'个计算完毕')

      with open(name+"_cal_ans.pickle","wb") as f:
              pickle.dump(scoredata,f)
              
def Ans(name,csv_name):
      # 加载结果
      with open("modle_save/"+name+"/"+name+"_cal_ans.pickle","rb") as f:
            scoredata = pickle.load(f)
      # 打开csv文件
      matedata_path = os.path.abspath(csv_name)
      f = open(matedata_path, encoding='utf-8')

      # 输出的csv文件    用日期作为文件名
      out = open("csv_save/"+name+"_"+csv_name[4:12]+"_data.csv","w")

      index = 0
      # 对csv文件的每一行
      csv_reader_lines = csv.reader(f)
      for one_line in csv_reader_lines:
            try :
                  output = ""
                  #得到时间戳
                  timestamp = one_line[0].replace(":","-")
                  index+=1
                  #将每一行的数据再组装起来
                  for each in one_line:
                        output+=each
                        output+=","
                  #第一行是列名
                  if index != 1:
                        output=output[:-1]+str(scoredata[timestamp][0]/1)
                  else:
                        output+=name
                        
                  out.writelines(output)
                  out.write("\n")
            except:
                  #无效的时间戳
                  print(timestamp)
                  
      f.close()
      out.close()
if __name__ == "__main__":
      rootpath = "modle_save/"
      
      filpaths = ["beautiful","boring",\
                  "depressing","lively","safety","wealthy"]
      #filpaths = ["beautiful"]
      #filpaths = ["boring"]
      #           南望山->未来城                光谷->南望山
      csv_name = ['VID_20191212_100933.mp4.csv','VID_20191229_133445.mp4.csv']
      video_name = ['video','video2']

      for i in range(2):
            for path in filpaths:
                  try:
                        Score(rootpath+path+"/"+path,video_name[i])
                        Ans(path,csv_name[i])
                  except:
                        print(str(i)+path)
                        continue
