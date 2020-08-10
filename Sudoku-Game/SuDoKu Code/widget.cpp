#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    //音乐线程
    mymusic = new Music;
    music_thread = new QThread(this);
    mymusic->moveToThread(music_thread);
    music_thread->start();

    ui->setupUi(this);
    this->setWindowTitle("数独");
    QPalette background;
    background.setBrush(QPalette::Background,QBrush(QPixmap("bc.png").scaled(700,560,Qt::IgnoreAspectRatio)));
    this->setPalette(background);//设置背景
    input = ' ';
    //初始化两个矩阵
    SDKMap.resize(9);
    for(auto &a:SDKMap)
        a.resize(9,'.');
    ANS.resize(9);
    for(auto &a:ANS)
        a.resize(9,'.');
    char num[9][9] = { {'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'} };
    W_and_B = 0;
    SIndex = 0;
    HardIndex = 4;
    SmallHardIndex = 0;
    timer = new QTimer(this);
    timer->start(1000);
    myclock = 600;
    STOP = false;
    SaveInBlack();
    ReadSQL();
    Easyer();
    connect(timer,&QTimer::timeout,this,&Widget::TimeOut);
    connect(this,&Widget::destroyed,[=](){ Delmusic();});//关掉窗口后结束线程
}

bool Widget::Deal()
{
    ChooseNode.x = -1;
    Solution a;
    return a.solveSudoku(ANS);
}

//继续计时
void Widget::TimeReStart()
{
    timer->start();
    STOP=false;
}

//时间暂停
void Widget::TimeStop()
{
    timer->stop();
    STOP=true;
}

//时间结束啦
void Widget::TimeOut()
{
    myclock--;
    update();
}

//得到一个ANS数组
void Widget::MakeAns()
{
    for(int i  =0;i<9;i++)
        for(int j = 0;j<9;j++)
        {
            ANS[i][j] = SDKMap[i][j];
        }
}

//清空游戏界面
void Widget::Clean()
{
    for(int i = 0;i<9;i++)
        for(int j = 0;j<9;j++)
            SDKMap[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
    SaveInBlack();
    RepealStack.clear();
    SIndex = 0;
}

//读取数独的数据
void Widget::ReadSQL()
{
    SQL.resize(5);
    for(auto &a:SQL)
    {
        a.resize(21);
        for(auto& b:a)
            b.resize(81,'.');
    }
    ifstream file("sql.txt");
    if(!file)
    {
        QMessageBox::information(NULL, "YING", "CantFind", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
        exit(0);
    }
    int index = 0;
    int index2 = 0;
    string line;
    while(getline(file, line))
    {
        if(line.length()==0)
        {
            index++;
            index2 = 0;
            continue;
        }
        for(int i =0;i<81;i++)
        {
            SQL[index][index2][i] = line[i];
            if(line[i]=='0')
                SQL[index][index2][i] = '.';
        }
        index2++;
    }

}

//提高难度
void Widget::Harder()
{
    SmallHardIndex++;
    if(SmallHardIndex>=20)
    {
        HardIndex++;
        if(HardIndex>=5)
        {
            HardIndex = 4;
            SmallHardIndex--;
        }
        else
            SmallHardIndex=0;
    }
    for(int i = 0;i<9;i++)
        for(int j = 0;j<9;j++)
        {
         ANS[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
         SDKMap[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
       }
    WrongWord.x = -1;
    ChooseNode.x = -1;
    myclock = 600;
    SaveInBlack();
    RepealStack.clear();
    update();
}


//降低难度
void Widget::Easyer()
{
    SmallHardIndex--;
    if(SmallHardIndex<0)
    {
        HardIndex--;
        if(HardIndex<0)
        {
            HardIndex = 0;
            SmallHardIndex++;
        }
        else
        {
            SmallHardIndex=19;
        }
    }
    for(int i = 0;i<9;i++)
        for(int j = 0;j<9;j++)
           {
            ANS[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
            SDKMap[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
          }

    WrongWord.x = -1;
    ChooseNode.x = -1;
    myclock = 600;
    SaveInBlack();
    RepealStack.clear();
    update();
}

//提交
bool Widget::Submit()
{

    //QMessageBox::information(NULL, "等一等!", "Content", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
    if(W_and_B!=81)
        return false;

    vector<int>viscal;
    vector<int>vislie;

    //遍历九宫格
    for(int i = 0;i<9;i+=3)
    {
        for(int j = 0;j<9;j+=3)
        {
            int cal[9]={0};
            for(int k = i;k<i+3;k++)
                for(int o = j;o<j+3;o++)
                {
                 if(SDKMap[k][o]!='.')
                 {
                    cal[SDKMap[k][o]-'1']++;
                    if(cal[SDKMap[k][o]-'1']>1)
                        {
                        WrongWord.x = k;
                        WrongWord.y = o;
                        return false;
                        }
                 }
               }
        }
    }

    //斜着遍历
    for(int i = 0;i<9;i++)
    {
        viscal.clear();
        vislie.clear();
        viscal.resize(9,0);
        vislie.resize(9,0);
         for(int j = 0;j<9;j++)
         {
             if(SDKMap[i][j]!='.')
             {
                 viscal[SDKMap[i][j]-'1']++;
                 if(viscal[SDKMap[i][j]-'1']>1){WrongWord.x = i;WrongWord.y = j;return false;}
             }
             if(SDKMap[j][i]!='.')
             {
                 vislie[SDKMap[j][i]-'1']++;
                 if(vislie[SDKMap[j][i]-'1']>1){WrongWord.x = i;WrongWord.y = j;return false;}
             }
         }
    }
    WrongWord.x = -1;
    return true;
}


Widget::~Widget()
{
    delete timer;
    delete ui;
}

//关掉音乐
void Widget::Delmusic()
{
    music_thread->quit();
    music_thread->wait();
}

//重写画画事件
void Widget::paintEvent(QPaintEvent *event)
{
    QPainter p(this);
    QFont font("Arial",20,QFont::Bold,true);
    p.setFont(font);

    for(int i = 1;i<=10;i++)
    {
        p.setPen(QPen(Qt::white,2));
        if((i-1)%3==0)
            p.setPen(QPen(Qt::white,5));
        p.drawLine(50*i,50,50*i,500);
        p.drawLine(50,50*i,500,50*i);
    }
    for(int i = 0;i<9;i++)
        for(int j = 0;j<9;j++)
        {
            if(SDKMap[i][j]!='.')
                p.drawText((i+1)*50,(j+1)*50,50,50,Qt::AlignCenter,QString(SDKMap[i][j]));
        }

    //绘制棋盘
    p.setPen(QPen(Qt::red,2));
    for(int i = 0;i<9;i++)
        for(int j = 0;j<9;j++)
        {
            if(ANS[i][j]!='.'&&SDKMap[i][j]!=ANS[i][j])
                p.drawText((i+1)*50,(j+1)*50,50,50,Qt::AlignCenter,QString(ANS[i][j]));
        }
    p.setPen(QPen(Qt::white,2));
    //

    //qDebug()<<ChooseNode.x;
    if(ChooseNode.x!=-1&&SDKMap[ChooseNode.x][ChooseNode.y]=='.')
        p.fillRect((ChooseNode.x+1)*50,(ChooseNode.y+1)*50,50,50,QBrush(Qt::white));
    QFont fontword("宋体",20,true);
    p.setFont(fontword);

    p.drawText(10*50+10,100,150,50,Qt::AlignCenter,QString("你好"));
    p.drawText(10*50+10,150,150,50,Qt::AlignCenter,QString("提交答案"));
    p.drawText(10*50+20,250,50,50,Qt::AlignCenter,QString("容易"));
    p.drawText(11*50+50,250,50,50,Qt::AlignCenter,QString("困难"));
    p.drawText(10*50+10,300,150,50,Qt::AlignCenter,QString("显示答案"));
    p.drawText(10*50+20,400,50,50,Qt::AlignCenter,QString("<-"));
    p.drawText(11*50+50,400,50,50,Qt::AlignCenter,QString("->"));
    p.drawText(350,10*50,150,50,Qt::AlignCenter,QString("清空"));
    p.drawText(20,0,100,50,Qt::AlignCenter,QString("休闲"));
    p.drawText(120,0,100,50,Qt::AlignCenter,QString("Normal"));
    p.drawText(220,0,100,50,Qt::AlignCenter,QString("MId"));
    p.drawText(320,0,100,50,Qt::AlignCenter,QString("困难"));
    p.drawText(420,0,100,50,Qt::AlignCenter,QString("爆裂"));
    if(myclock!=0)
    {
        if(STOP)
            p.drawText(10*50+10,500,150,50,Qt::AlignCenter,QString("时间暂停"));
        else
            p.drawText(10*50+10,500,150,50,Qt::AlignCenter,QString(QString("%1").arg(myclock)));
    }
    else
        p.drawText(10*50+10,500,150,50,Qt::AlignCenter,QString("时间结束"));
    //黑色数字覆盖原来的白色数字
    QFont fontwhite("Arial",20,QFont::Bold,true);
    p.setFont(fontwhite);
    p.setPen(QPen(Qt::black,2));
    for(int k  = 0;k<BlackWord.size();k++)
    {
        int i = BlackWord[k].x;
        int j = BlackWord[k].y;
        p.drawText((i+1)*50,(j+1)*50,50,50,Qt::AlignCenter,QString(SDKMap[i][j]));
    }
    QString level;
    switch (HardIndex) {
    case 0:
        level = "休闲 ";
        break;
    case 1:
        level = "普通 ";
        break;
    case 2:
        level = "中等 ";
        break;
    case 3:
        level = "困难 ";
        break;
    case 4:
        level = "爆裂 ";
        break;
    default:
        break;
    }
    p.setFont(fontword);
    p.drawText(10*50+10,0,150,50,Qt::AlignCenter,QString("当前难度"));
    p.drawText(10*50+10,50,90,50,Qt::AlignCenter,QString(level));
    p.drawText(11*50+10,50,90,50,Qt::AlignCenter,QString("%1").arg(SmallHardIndex+1));
    p.drawText(10*50+40,350,90,50,Qt::AlignCenter,QString("撤销"));
    p.drawText(10*50+10,200,150,50,Qt::AlignCenter,QString("更换难度"));
    p.drawText(10*50+10,450,150,50,Qt::AlignCenter,QString("已用时间"));
    p.drawText(30,10*50,250,50,Qt::AlignCenter,QString("当前选中位置"));
    if(ChooseNode.x!=-1){
        p.drawText(250,10*50,30,50,Qt::AlignCenter,QString("%1").arg(ChooseNode.x));
        p.drawText(280,10*50,10,50,Qt::AlignCenter,",");
        p.drawText(290,10*50,30,50,Qt::AlignCenter,QString("%1").arg(ChooseNode.y));
    }
    else
         p.drawText(250,10*50,50,50,Qt::AlignCenter,"无 ");
    //右边的线
    p.drawLine(500+150+10,0,500+150+10,550);
    p.drawLine(500+10,50,500+10,550);
    for(int i = 0;i<=11;i++)
        p.drawLine(510,i*50,660,i*50);

    if(WrongWord.x!=-1)
    {
        int i = WrongWord.x;
        int j = WrongWord.y;
        p.drawText((i+1)*50,(j+1)*50,50,50,Qt::AlignCenter,QString(SDKMap[i][j]));
        p.setPen(QPen(Qt::blue,2));
    }

}

//保存到黑色里面
void Widget::SaveInBlack()
{
    BlackWord.clear();
    SDKNode work;
    for(int i  =0;i<9;i++)
        for(int j = 0;j<9;j++)
        {
            if(SDKMap[i][j]!='.')
            {
                work.x = i;
                work.y = j;
                W_and_B++;
                BlackWord.push_back(work);
            }
        }
}

//检查当前结点是否是黑色的
bool Widget::Check(int x, int y)
{
     for(int i = 0;i<BlackWord.size();i++)
     {
         if(BlackWord[i].x==x&&BlackWord[i].y==y)
             return false;
     }
     return true;
}

//向左回退
void Widget::RepealLeft()
{
    SIndex--;
    if(SIndex<0)
    {
        SIndex = 0;return ;
    }
    int x,y;
    char his;
    x = RepealStack[SIndex].x;
    y = RepealStack[SIndex].y;
    his = RepealStack[SIndex].his;
        SDKMap[x][y] = his;
    //qDebug()<<"now"<<SIndex<<" "<<x<<" "<<y<<" "<<his;
}



//向右回退
void Widget::RepealRight()
{
    if(SIndex>=RepealStack.size())
    {
        SIndex = RepealStack.size();
        return ;
    }
    int x,y;
    char now;
    x = RepealStack[SIndex].x;
    y = RepealStack[SIndex].y;
    now = RepealStack[SIndex].now;
    SDKMap[x][y] = now;
    SIndex++;
    //qDebug()<<"now"<<SIndex<<" "<<x<<" "<<y<<" "<<now;
}


//鼠标点击事件
void Widget::keyPressEvent(QKeyEvent *event)
{
    //判断操作
    bool pan = true;
    switch (event->key())
       {
   case Qt::Key_1:case Qt::Key_Launch1:
         input = '1';
         //qDebug()<<input;
         break;
    case Qt::Key_2:case Qt::Key_Launch2:
         input = '2';
         //qDebug()<<input;
         break;
    case Qt::Key_3:case Qt::Key_Launch3:
         input = '3';
         //qDebug()<<input;
         break;
    case Qt::Key_4:case Qt::Key_Launch4:
         input = '4';
         //qDebug()<<input;
         break;
    case Qt::Key_5:case Qt::Key_Launch5:
         input = '5';
         //qDebug()<<input;
         break;
    case Qt::Key_6:case Qt::Key_Launch6:
         input = '6';
         //qDebug()<<input;
         break;
    case Qt::Key_7:case Qt::Key_Launch7:
         input = '7';
         //qDebug()<<input;
         break;
    case Qt::Key_8:case Qt::Key_Launch8:
         input = '8';
         //qDebug()<<input;
         break;
    case Qt::Key_9:case Qt::Key_Launch9:
         input = '9';
         //qDebug()<<input;
         break;
    case Qt::Key_Delete:
    case Qt::Key_Backspace:
         input = '.';
         //qDebug()<<input;
         break;
       default:
        //无效操作
        pan = false;
           break;
       }
    //有效操作
    if(pan)
        if(ChooseNode.x != -1)
        {
             RepealNode work;
            //放置用户的输入
            work.his = SDKMap[ChooseNode.x][ChooseNode.y];
            work.now = input;
            work.x = ChooseNode.x;
            work.y = ChooseNode.y;
            SDKMap[ChooseNode.x][ChooseNode.y]=input;
            if(input=='.')
                W_and_B--;
            else
                W_and_B++;



            if(SIndex<RepealStack.size())
                RepealStack[SIndex] = work;
            else
                RepealStack.push_back(work);
            SIndex++;
            ChooseNode.x = -1;
            //qDebug()<<"size :"<<RepealStack.size();
    }

    update();
}

//鼠标点击事件
void Widget::mousePressEvent(QMouseEvent *event)
{
    int x = event->x(),y = event->y();
    if(STOP==false)
    {
        //qDebug()<<x<<" "<<y;
        //如果在棋盘上
        if(x>50&&x<500&&x%50)
            if(y>50&&y<500&&y%50)
            {
                if(Check(x/50-1,y/50-1))
                {
                    x = x/50-1;y=y/50-1;
                    ChooseNode.x = x;
                    ChooseNode.y = y;
                    //qDebug()<<x<<" "<<y;
                }
            }

    }
    //如果在更换难度的界面上
    if(y>0&&y<50&&x>20&&x<520)
    {
        HardIndex = ((x+80)/100)-1;
        SmallHardIndex = 0;
        //qDebug()<<"NOW"<<HardIndex<<" "<<SmallHardIndex;
        for(int i = 0;i<9;i++)
            for(int j = 0;j<9;j++)
               {
                ANS[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
                SDKMap[i][j] = SQL[HardIndex][SmallHardIndex][i*9+j];
              }
        WrongWord.x = -1;
        ChooseNode.x = -1;
        myclock = 600;
        SaveInBlack();
        RepealStack.clear();
    }

    //如果在别的命令上
    if(x>10*50+10&&x<10*50+10+150)
    {
        if(y<500&&y%50)
        {
            switch (y/50) {
            case 2:
                //qDebug()<<"重新开始";
                //重新开始的函数
                break;
            case 3:
            {
                //qDebug()<<"提交答案";
                int cal = 0;
                for(int i = 0;i<9;i++)
                    for(int j  =0;j<9;j++)
                        if(ANS[i][j]!='.')
                            cal++;
                if(cal==81)break;
                if(Submit())
                    QMessageBox::StandardButton r = QMessageBox::question(this, "恭喜", "答案正确", QMessageBox::Yes | QMessageBox::No, QMessageBox::No);
                else
                {
                    if(W_and_B!=81)
                        QMessageBox::StandardButton r = QMessageBox::question(this, "Stop", "Havent Fininshed", QMessageBox::Yes | QMessageBox::No, QMessageBox::No);
                    else
                        QMessageBox::StandardButton r = QMessageBox::question(this, "OHNO", "WRONG ", QMessageBox::Yes | QMessageBox::No, QMessageBox::No);
                }
                //提交答案的函数
                break;
            }
            case 5:
                if(x/50==10)
                {
                    //qDebug()<<"降低难度";
                    //降低难度的函数
                    Easyer();
                }
                else if(x/50==12)
                {
                    //qDebug()<<"增加难度";
                    //增加难度的函数
                    Harder();
                }
                break;
            case 6:
            {
                //qDebug()<<"显示答案";
                //显示答案的函数
                if(Deal()==false)
                    QMessageBox::information(NULL, "Not OK", "No Value", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
                timer->stop();
                STOP = true;
                RepealStack.clear();
                break;
            }
            case 8:
                if(x/50==10)
                {
                    //qDebug()<<"向后撤销";
                    //降低难度的函数
                    RepealLeft();
                }
                else if(x/50==12)
                {
                    //qDebug()<<"向前撤销";
                    //增加难度的函数
                    RepealRight();
                }
                break;
            default:
                break;
            }
        }
    }
    //清空棋盘
    //p.drawText(400,10*50,150,50,Qt::AlignCenter,QString("清空棋盘"));
    if(x>350&&x<500&&y>10*50&&y<11*50)
        Clean();
    //暂停时间
    if(x>10*50+10&&x<10*50+10+150&&y>500&&y<550)
    {
        //qDebug()<<"提交答案";
        int cal = 0;
        for(int i = 0;i<9;i++)
            for(int j  =0;j<9;j++)
                if(ANS[i][j]!='.')
                    cal++;
        if(cal==81)return;
        if(STOP==false)
            TimeStop();
        else
            TimeReStart();
    }

    update();
}
