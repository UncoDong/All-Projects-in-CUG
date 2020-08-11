from AWS.SQSVister import *




for i in range(1):
      print(str('----'+str(i))*5)
      a = [SQSVisiter('SZZS'),SQSVisiter('CJL'),\
     SQSVisiter('ThreeLayer'),SQSVisiter('JJ')]
      for each in a:
            each.GetMessage()
            each.DelMessage()
            each.GetMessage()
            print('------')
            
