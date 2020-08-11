import pymssql
      
class SQLVisiter:
      #链接数据库
      conn = None

      #要操作的数据库
      cursor = None
      
      def __init__(self,ht,ur,pwd,dbname):
            self.conn = pymssql.connect(ht,ur,pwd,dbname)
            self.cursor = self.conn.cursor()

      def Search(self,sql='select * from Data'):
            self.cursor.execute(sql)
            return self.cursor.fetchall()
            

host = "127.0.0.1:1433"# 本地服务器
user = "sa" #连接帐号
password = "123456"# 连接密码


DBname = 'company'

if __name__ == '__main__':
      SQL = SQLVisiter(host,user,password,DBname)
      res = SQL.Search()
