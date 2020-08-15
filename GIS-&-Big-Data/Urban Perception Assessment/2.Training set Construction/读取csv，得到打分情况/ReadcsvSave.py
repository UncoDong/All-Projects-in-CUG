'''
功能：读取csv文件，得到对每张图片的打分情况
'''

import os
import csv
import pickle

# 形成 文件名：分数 的一一对应关系
data = {}
# 得到map对应
def GetMap(matedata_path):
      data.clear()#每次清空数据
      if os.path.exists(matedata_path):
          with open(matedata_path, encoding='utf-8') as f:
              # 得到打开的csv文件的内容
              csv_reader_lines = csv.reader(f)
              # 遍历每一行
              for one_line in csv_reader_lines:
                  #每行的第一个元素都是文件名
                  if one_line[0] == 'filename':
                        continue
                  data[one_line[0]] = one_line[1]
              print('{} total lines : {:d} map size{:d}'.format(str(matedata_path), len(data), len(data)))
      else:
          print('matedata_path is wrong...' + matedata_path)
          exit(1)
          
if __name__ == '__main__':       
      # 保存文件的路径
      if os.path.exists('csv_message') == False:
            os.mkdir('csv_message')
      # 文件列表
      filpaths = ["beautiful","boring",\
            "depressing","lively","safety","wealthy"]
      #遍历每一个文件
      for filname in filpaths:
            GetMap("auto_save_scores_"+filname+".csv")
            #保存文件为pickle类型
            with open('csv_message\\'+filname+'_csv_message.pickle','wb') as f:
                  pickle.dump(data,f)
