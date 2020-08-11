from tkinter import *
from AWS.SQSVister import *
import _thread
import time
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
class Cilent:
      
      def PltMany(self,res_list,title,legend):
            plt.xlabel('日期')
            plt.ylabel('价格/元')
            for i in range(len(legend)):
                  if legend[i] == 'y1':
                        legend[i] = '开盘价'
                  elif legend[i] == 'y2':
                        legend[i] = '最高价'
                  elif legend[i] == 'y3':
                        legend[i] = '最低价'
                  elif legend[i] == 'y4':
                        legend[i] = '收盘价'
            print(legend)
            plt.title(title)
            
            mid = range(1,len(legend[0]),300)
            x_tick = [res_list[0][each] for each in mid]            
            plt.xticks(mid,x_tick)
            
            for i in range(len(res_list)-1):
                  plt.plot(res_list[i+1])
            plt.legend(legend)
            plt.show()
      
      #就绘制俩图
      def Pltxy(self,x,y,title):
            plt.xlabel('日期')

            if title == 'JJ':
                  plt.title('均价')
                  plt.ylabel('均价/元')
            else:
                  plt.title('上证指数')
                  plt.ylabel('指数点')
            #print(len(x))
            mid = range(1,len(x),300)
            x_tick = [x[each] for each in mid]            
            plt.xticks(mid,x_tick)
            plt.plot(y)
            plt.show()


      def Deal(self,res,name):
            if 'y'in name:
                  return np.array(res[1:],dtype=np.float64)
            elif name == 'x':
                  return np.array(res[1:])
            
      
      #处理x和y
      def DealXY(self,res1,res2):
            res1 = res1.split()
            res2 = res2.split()
            if res1[0] == 'x':
                  X = self.Deal(res1,'x')
                  Y = self.Deal(res2,'y')
            else:
                  Y = self.Deal(res1,'y')
                  X = self.Deal(res2,'x')
            return X,Y

      #接收全部的
      def Recive(self,name):
            pan = True
            res = []
            while pan:
                  SQS = SQSVisiter(name)
                  res = SQS.GetMessage()
                  if name == 'JJ' or name == 'SZZS':
                        if len(res)==2:
                              pan = False
                              X,Y = self.DealXY(res[0],res[1])
                              self.Pltxy(X,Y,name)
                              SQS.DelMessage()
                        elif len(res)>2:
                              print('列表内元素有误，请重试')
                              SQS.DelMessage()
                              
                  elif name == 'CJL':
                        legend = []
                        if len(res)==5:
                              pan = False
                              #调换顺序
                              for i in range(len(res)):
                                    legend.append(res[i][0]+res[i][1])
                                    
                                    pan = res[i][0]
                                    res[i] = self.Deal(res[i].split(),pan)
                                    if pan == 'x':
                                          change = res[0]
                                          res[0] = res[i]
                                          res[i] = change

                              legend.remove('x ')
                              self.PltMany(res,name,legend)
                              SQS.DelMessage()       
                        elif len(res)>5:
                              print('列表内元素有误，请重试')
                              SQS.DelMessage()
                        
                        
                  
                  time.sleep(5)
      


      def SearchSZZS(self):
            SQSLayer = SQSVisiter('ThreeLayer')
            _thread.start_new_thread(SQSLayer.SendMessage,('S SearchMessage',))
            print('查询上证指数中...')
            _thread.start_new_thread(self.Recive,('SZZS',))
            
      def SearchCJL(self):
            SQSLayer = SQSVisiter('ThreeLayer')
            _thread.start_new_thread(SQSLayer.SendMessage,('C SearchMessage',))
            print('查询成交量中...')
            _thread.start_new_thread(self.Recive,('CJL',))

      def SearchJJ(self):
            SQSLayer = SQSVisiter('ThreeLayer')
            _thread.start_new_thread(SQSLayer.SendMessage,('J SearchMessage',))
            print('查询均价中...')
            _thread.start_new_thread(self.Recive,('JJ',))
            
      
      def __init__(self):
            self.root = Tk()
            self.root.title('客户端')

            self.bt_JJ = Button(self.root,text='均价',command=self.SearchJJ,font = ('黑体',12))
            self.bt_JJ.pack()
            
            self.bt_SZZS = Button(self.root,text='上证指数',command=self.SearchSZZS,font = ('黑体',12))
            self.bt_SZZS.pack()

            self.bt_CJL = Button(self.root,text='成交量',command=self.SearchCJL,font = ('黑体',12))
            self.bt_CJL.pack()
            
            
            self.root.mainloop()

if __name__ == '__main__':
      client = Cilent()
