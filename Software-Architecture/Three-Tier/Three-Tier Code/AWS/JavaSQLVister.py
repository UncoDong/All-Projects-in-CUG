import jpype
import os

class JavaSQLVisiter:
      #数据库本体
      instance = None

      def __init__(self):
            jarpath = os.path.join(os.path.abspath('.'), 'D:\\myjava\\ConnectSQL\\test_connectsql.jar')
            #dependency = os.path.join(os.path.abspath('.'), 'F:/JPypeTestl/dependency')
            jpype.startJVM("D:\\Program Files\\Java\\jdk1.8.0_221\\jre\\bin\\server\\jvm.dll", "-ea", "-Djava.class.path=%s" %jarpath)#,"-Djava.ext.dirs=%s" %dependency)    #当有依赖的JAR包存在时，一定要使用-Djava.ext.dirs参数进行引入
            JClass = jpype.JClass('SQL.connect')
            self.instance = JClass()
            s = self.instance.connect_sql()
            print(s)
            #result = (instance.SQLTest())
      def Search(self,input_):
            try:
                  print('开始查询'+input_)
                  result = (self.instance.build_search(input_))
                  print('查询'+input_+'完成')
                  return list(result)
            except BaseException:
                  print('出现异常')
      def __del__(self):
            jpype.shutdownJVM()


      
if __name__ == '__main__':
      SQL = JavaSQLVisiter()
      pass
      
      #res = SQL.Search('日期')
      #print(res[0])
