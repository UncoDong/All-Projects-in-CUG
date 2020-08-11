from tkinter import *
from AWS.SQSVister import *
from AWS.JavaSQLVister import *
import _thread
import time
import jpype
import os


class Work:
      sql = JavaSQLVisiter()
      def __init__(self):
            print('业务逻辑启动')

      #处理值
      def ReturnValue(self,res,str_output):
            str_output = str_output+' '
            for i in range(len(res)):
                  charu = ''.join(str(res[i]))
                  if 'N/A' in charu:
                        charu = '0'
                  str_output = str_output + charu + ' '
            return str_output

            
      #发送值
      def Send(self,my_list,which):
            print('发送到'+which)
            if which == 'J':
                  SQS = SQSVisiter('JJ')    
            elif which == 'S':
                  SQS = SQSVisiter('SZZS')
            elif which == 'C':
                  SQS = SQSVisiter('CJL')
                  
            for each in my_list:
                  SQS.SendMessage(each)
      
      #访问数据库
      def VisSQL(self,which):
            print(which)
            if which == 'J':
                  res1 = self.sql.Search('日期')
                  res2 = self.sql.Search('均价')

                  x = self.ReturnValue(res1,'x')
                  y = self.ReturnValue(res2,'y')

                  self.Send([x,y],which)
                  
            
            elif which == 'S':
                  res1 = self.sql.Search('日期')
                  res2 = self.sql.Search('总市值')
                  
                  another_y = []
                  ans = 100
                  front = (float)(res2[0])
                  for each in res2:
                        each = (float)(each)
                        another_y.append(ans*(1.0+(each-front)/(front*1.0)))
                        ans = another_y[len(another_y)-1]
                        front = each
                  x = self.ReturnValue(res1,'x')
                  y = self.ReturnValue(another_y,'y')

                  self.Send([x,y],which)

                  
            
            elif which == 'C':
                  
                  res0 = self.sql.Search('日期')
                  res1 = self.sql.Search('开盘价')
                  res2 = self.sql.Search('最高价')
                  res3 = self.sql.Search('最低价')
                  res4 = self.sql.Search('收盘价')

                  res0 = self.ReturnValue(res0,'x')
                  res1 = self.ReturnValue(res1,'y1')
                  res2 = self.ReturnValue(res2,'y2')
                  res3 = self.ReturnValue(res3,'y3')
                  res4 = self.ReturnValue(res4,'y4')

                  self.Send([res0,res1,res2,res3,res4],which)
                  


      
               
      #一直接收消息
      def ReciveMessage(self):
            while True:
                 SQSLayer = SQSVisiter('ThreeLayer')
                 print('开始接收消息')
                 rt = SQSLayer.GetMessage()
                 if rt != []:
                       for each in rt:
                             print(each)
                             self.VisSQL(each[0])
                             
                       SQSLayer.DelMessage()
                 time.sleep(5)
            

if __name__ == '__main__':
      work = Work()
      #work.VisSQL('C')
      work.ReciveMessage()
