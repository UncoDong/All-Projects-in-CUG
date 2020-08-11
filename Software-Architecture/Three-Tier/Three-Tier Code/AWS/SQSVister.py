import boto3
class SQSVisiter:
      #队列初始化
      sqs = None
      
      #队列名字
      name = None
      
      #队列本列
      queue = None

      #结果字符串
      result = "空值"

      #消息列表
      message_list = []
      
      #构造函数
      def __init__(self,name):
            self.name = name
            
            try:
                self.sqs = boto3.resource('sqs')
                self.queue = self.sqs.get_queue_by_name(QueueName=self.name)
                print(self.name+'已建立')
            except BaseException:
                  self.result = "对%s的初始化错误"%self.name
                  print(self.result)
                  exit(0)
                  
      #发送信息函数
      def SendMessage(self,message):
            self.queue.send_message(MessageBody=message)
            if len(message)>10:
                  message = message[:10]+'...'
            self.result = "%s发送成功"%message
            print(self.result)

      #得到全部消息
      def GetMessage(self):
            while True:
                  mid = self.queue.receive_messages(MessageAttributeNames=['Author'])
                  #print(mid)
                  if mid != []:
                      self.message_list.append(mid[0])
                      charu = ''
                      if(len(mid[0].body)>10):
                            charu = '...'
                      print(mid[0].body[0:10]+charu+'查询成功')
                  else:
                      break
            messages = []
            for i in range(len(self.message_list)):
                  message = self.message_list[i].body
                  messages.append(message)
                  #print(messages[i])
                  
            if messages == []:
                  print('队列为空')
            return messages

      #删除全部消息
      def DelMessage(self):
            while len(self.message_list) > 0 :
                  message = self.message_list[0]
                  charu = ''
                  if(len(message.body)>10):
                      charu = '...'
                  print(message.body[:10]+charu+'已删除')
                  message.delete()
                  self.message_list.remove(message)
            print(self.name+'已清空')

      #析构函数 也是删除
      def __del__(self):
            #self.DelMessage()
            print(self.name+'调用析构')

      #测试发送很多消息
      def TestSend(self):
            for i in range(5):
                  self.SendMessage(str(i))
                    
            
if __name__ == '__main__':
      SQS = SQSVisiter('UncleDong')
      SQS.TestSend()
      a = SQS.GetMessage()
      del SQS
