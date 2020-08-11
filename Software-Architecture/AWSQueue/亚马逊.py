from tkinter import *
from PIL import ImageTk, Image
import time
import webbrowser
import boto3
import _thread

#------------------登录界面--------------
def LoginBar():
    root = Tk()
    root.title('登录')
    root.resizable(width=False, height=False)

    #背景图
    canvas = Canvas(root, width=360,height=240,bd=0, highlightthickness=0)
    imgpath = '素材/登录界面.png'
    img = Image.open(imgpath)
    photobg = ImageTk.PhotoImage(img)
    canvas.create_image(180, 120, image=photobg)
    canvas.pack()

    #创立PhotoImage对象
    photo = PhotoImage(file = "素材/头像.png")
    HeadPhoto = Label(root,image = photo)

    #创建动态字符串
    var = StringVar()
    var.set('登陆中')

    #文字
    textLabel = Label(root,bg = 'white',textvariable = var,font=("宋体",20))
    textLabel.pack()

    #在背景上创建窗口
    canvas.create_window(190, 75, width=100, height=100,window=HeadPhoto)#头像
    canvas.create_window(190, 145, width=200, height=40,window=textLabel)#文字框

    #定义登录函数
    def Login():
      import boto3
      try:
           
            global sns
            sns = boto3.client('sns')
            print('连上了连上了')
            var.set('连上了连上了')
            root.destroy()
            User()
            return True
      except BaseException:
            print('登录不上啊')
            messagebox.showerror('登录失败','请重新设置用户名和密码')
            exit(0)
            return False      
    _thread.start_new_thread(Login,())
    root.mainloop()

#----------用户界面-----------
def User():
    global root
    root = Tk()
    root.title('用户界面')
    root.resizable(width=False, height=False)
    
    #背景图
    canvas = Canvas(root, width=400,height=300,bd=0, highlightthickness=0)
    imgpath = '素材/用户背景.png'
    img = Image.open(imgpath)
    photobg = ImageTk.PhotoImage(img)
    canvas.create_image(180, 120, image=photobg)
    canvas.pack()

    #创立PhotoImage对象
    photo = PhotoImage(file = "素材/头像.png")
    headphoto = Label(root,image = photo)

    #创建动态字符串
    var = StringVar()
    var.set( 'arn:aws:sns:us-east-1:068066148184:WeiXin')

    # 创建滚动条
    scroll = Scrollbar()
    
    #创建文本框
    text_message = Text(root,width=200,height=25)
    scroll.config(command=text_message.yview)
    text_message.config(yscrollcommand=scroll.set)

    #输入ARN
    entry_arn = Entry(root,insertbackground='blue', highlightthickness =0,textvariable =  var)

    def open_url():
        webbrowser.open("https://mail.qq.com/", new=0)
        
    def create_sqs():
        root.destroy()
        sqsbox()
        #_thread.start_new_thread(sqsbox,())

    def sending(message):
        print(message)
        if message != '':
            pass
        global sns
        try:
            sns.publish(TopicArn=entry_arn.get(),
                           Message=message,Subject='string',MessageStructure='string',)
        except BaseException:
            print('又连不上了')
            messagebox.showerror('连不上啊','请重新设置用户名和密码')
            exit(0)
            
        text_message.delete('1.0','end')
        text_message.insert(END,'发送成功！')
        
    def send_message():
        message = (text_message.get("0.0","end").replace(" ","")).strip("\n")
        _thread.start_new_thread(sending,(message,))
        text_message.insert(END,'\n发送中...\n')
        

        
        
    #添加按钮
    but_mail = Button(root,text = '邮箱查询',command = open_url,bd=0,bg = 'white',fg = 'black',font = ('黑体',12))
    but_sqs = Button(root,text = 'SQS查询',command = create_sqs,bd=0,bg = 'white',fg = 'black',font = ('黑体',12))
    but_send = Button(root,text = '发送消息',command = send_message,bd=0,bg = 'white',fg = 'black',font = ('黑体',12))
    
    
    #在背景上创建窗口
    canvas.create_window(75, 75, width=100, height=100,window=headphoto)#头像
    canvas.create_window(250, 100, width=200, height=50,window=text_message)#输入文本
    canvas.create_window(360, 100, width=10, height=50,window=scroll)#滚动条
    canvas.create_window(200, 200, width=300, height=25,window=entry_arn)#ARN输入框
    canvas.create_window(200, 150, width=100, height=25,window=but_send)#邮箱查询按钮
    canvas.create_window(120, 240, width=100, height=25,window=but_mail)#邮箱查询按钮
    canvas.create_window(270, 240, width=100, height=25,window=but_sqs)#邮箱查询按钮


    root.mainloop()

def sqsbox():
    
    rootsqs = Tk()
    rootsqs.title('队列接收')
    message_list = []
    #背景图
    canvas = Canvas(rootsqs, width=400,height=300,bd=0, highlightthickness=0)
    imgpath = '素材/注册界面.png'
    img = Image.open(imgpath)
    photobg = ImageTk.PhotoImage(img)
    canvas.create_image(180, 120, image=photobg)
    canvas.pack()

    #创建动态字符串
    var_name = StringVar()
    var_name.set( 'UncleDong')
    
    #输入队列名字
    entry_name=Entry(rootsqs,insertbackground='blue', highlightthickness =2,textvariable =  var_name)

    # 创建滚动条
    scroll2 = Scrollbar()

    #接受队列消息的文本框
    text_message2 = Text(rootsqs,width=200,height=25)
    scroll2.config(command=text_message2.yview)
    text_message2.config(yscrollcommand=scroll2.set)

    #得到队列消息
    def searching():
        print(entry_name.get())
        pass
        sqs = boto3.resource('sqs')
        queue = sqs.get_queue_by_name(QueueName=entry_name.get())
        print(queue.url)
        while True:
            mid = queue.receive_messages(MessageAttributeNames=['Author'])
            print(mid)
            if mid != []:
                message_list.append(mid[0])
            else:
                break
        text_message2.delete('1.0','end')
        text_message2.insert(END,'查询成功！\n\n')
        for message in message_list:
            text_message2.insert(END,message.body+'\n')
            
    def search_sqs():
        message_list.clear()
        text_message2.delete('1.0','end')
        _thread.start_new_thread(searching,())
        text_message2.insert(END,'查询中...\n')
    
    #删除队列消息
    def delete_sqs():
        pan = messagebox.askyesno('提示', '要删除所有消息么？')
        if pan ==True:
            for message in message_list:
                message.delete()
            text_message2.delete('1.0','end')
            messagebox.showinfo('提示','删除完成')
        
    
    #查询按钮和删除按钮
    
    but_search = Button(rootsqs,text = '查询',command = search_sqs,bd=0,bg = 'white',fg = 'black',font = ('黑体',12))
    but_delete = Button(rootsqs,text = '删除',command = delete_sqs,bd=0,bg = 'white',fg = 'black',font = ('黑体',12))

    
    
    #在背景上创建窗口
    canvas.create_window(240, 75, width=200, height=25,window=entry_name)#输入队列名字
    canvas.create_window(200, 150, width=300, height=100,window=text_message2)#队列返回值文本
    print('hi')
    canvas.create_window(360, 150, width=10, height=100,window=scroll2)#滚动条
    
    canvas.create_window(130, 240, width=100, height=25,window=but_search)#查询按钮
    canvas.create_window(270, 240, width=100, height=25,window=but_delete)#删除按钮  
    
    rootsqs.mainloop()
    

if __name__ == '__main__':
      #sqsbox()
      #User()
      LoginBar()
      
