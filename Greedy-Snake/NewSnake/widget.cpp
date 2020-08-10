#include "widget.h"
#include "ui_widget.h"
//生成随机数
int RangedRandDemo( int range_min, int range_max)
{
    /*
    作者：--Allen-- 来源：CSDN 原文：https blog.csdn.net/q1007729991/article/details/38469603
    版权声明：本文为博主原创文章，转载请附上博文链接！
    */
      int u = (double)rand() / (RAND_MAX + 1) *(range_max - range_min) // RAND_MAX = 32767
            + range_min;
      return u;
}

//数字转换成q字符串
QString numtoqstr(int num)
{
    stringstream ss;
    ss<<num;
    return QString::fromStdString(ss.str())  ;
}

//字符串转换成q字符串
QString strtoqstr(string str)
{
     return QString::fromStdString(str)  ;
}

//排序用的比较
bool cmp(const WORD&a, const WORD&b)
{
    return a.word.length() < b.word.length();
}

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    //背景的一系列操作
    setFixedSize(1000,750);
    this->autoFillBackground();
    QPalette background;
    background.setBrush(QPalette::Background,QBrush(QPixmap("image/游戏背景.png").scaled(1000,750,Qt::IgnoreAspectRatio)));
    this->setPalette(background);

    //初始化分数和关卡
    Sorce = 0;
    life = 3;
    Level = 1;

    //杂七杂八的初始化
    press = false;
    life = 1 ;
    applindex = 0;
    fangxiang = 2;
    GetWord();
    word_dangqian = 0;//初始单词的下标
    word = MyWord[Level-1][word_dangqian].word;
    QFont font("Microsoft YaHei",14);//设置字体
    GameStop = false;//游戏没有停止
    Speed = 500;//设置初始速度

    //开场动画
    //a.show();

    //创建音乐线程
    musictype = 1;//开场音乐
    mymusic = new Music;
    music_thread = new QThread(this);
    mymusic->moveToThread(music_thread);

    //播放音乐
    connect(&a,&Start_Action::beginstartmusic,[=]()
    {
        music_thread->start();
        mymusic->chose(musictype);
    });

    //开始定时
    timer = new QTimer;
    timer->stop();
    connect(timer,&QTimer::timeout,[&](){SnakeMove();update();});

    //设置最开始的蛇的坐标
    mysnake.head->x = 1;mysnake.head->y = 0;
    Body body;body.x = 0,body.y = 0;
    mysnake.InsertHead(body);

    //初始化地图
    memset(Map,0,16*25*sizeof(int));
    Map[0][0] = -1;//身子
    Map[0][1] = -1;//脑袋
    SetApple(word);//苹果

    //读取苹果和蛇的图片
    QString adress = "image/apple/AppleA.png";
    string str;
    str = adress.toStdString();
    str [17]--;
    for(int i=1;i<=26;i++)
    {
        str [17]+=1;
        adress = QString::fromStdString(str);
        StrAppleImage[i]=adress;
    }
    StrHead="image/snake/sh02.png";
    StrBody="image/snake/sb0202.png";

    //减一条生命的死亡窗口
    QWidget *life_window = new QWidget;//新建窗口
    QPushButton *life_ok = new QPushButton(life_window);//新建摁钮
    QLabel* life_word = new QLabel(life_window);//新建文字
    life_window->resize(500,250);//窗口大小
    life_window->setWindowTitle("Oh!NO!");//窗口的标头文字
    life_word->setGeometry(100,50,400,50);//文字位置
    life_word->setText(QString("小蛇死了,生命-1"));//文字内容
    life_word->setFont(font);//文字字体
    life_ok->setText("I know it");
    life_ok->setGeometry(201,150,100,50);

    //游戏结束的死亡窗口
    QWidget *dead_window = new QWidget;//新建窗口
    QPushButton *dead_ok = new QPushButton(dead_window);//新建摁钮
    QPushButton *dead_no = new QPushButton(dead_window);//新建摁钮
    QLabel* dead_word = new QLabel(dead_window);//新建文字
    dead_window->resize(500,250);//窗口大小
    dead_window->setWindowTitle("DIE AGAIN");//窗口的标头文字
    dead_word->setGeometry(100,50,400,50);//文字位置
    dead_word->setText(QString("Restart?"));//文字内容
    dead_word->setFont(font);//文字字体
    dead_ok->setText("Yeah");
    dead_ok->setGeometry(75,150,100,50);
    dead_no->setText("NO");
    dead_no->setGeometry(325,150,100,50);

    //接收信号的操作
    connect(this,&Widget::DIED_life,[=](){timer->stop();musictype = 3; mymusic->chose(musictype);life_window->show();});//-1命时弹出窗口
    connect(life_ok,&QPushButton::clicked,[=](){life_window->close();Rebegin(); life--;SetApple(word);});//-1命窗口继续游戏
    connect(this,&Widget::GameStart,[=](){timer->start(Speed);});
    connect(this,&Widget::DIED_end,[=](){timer->stop(); dead_window->show();musictype = 3; mymusic->chose(musictype);});//死亡时弹出窗口

    connect(dead_ok,&QPushButton::clicked,[=](){ dead_window->close();Regame();});
    connect(dead_no,&QPushButton::clicked,[=](){ dead_window->close();this->close();});//不要重新开始游戏

    connect(this,&Widget::destroyed,[=](){ Delmusic();});//关掉窗口后结束线程

    connect(&a,&Start_Action::START,[=](){ a.close();this->show();timer->start(Speed); musictype = 2; mymusic->chose(musictype);});//开场动画结束后进入游戏 即关掉开场动画窗口，计时器开始计时

    connect(ui->Fast,&QRadioButton::toggled,this,&Widget::Speed_Fast);//变快速
    connect(ui->Midu,&QRadioButton::toggled,this,&Widget::Speed_Midu);//变中速
    connect(ui->Slow,&QRadioButton::toggled,this,&Widget::Speed_Slow);//变慢速
}

//关掉音乐
void Widget::Delmusic()
{
    music_thread->quit();
    music_thread->wait();
}

void Widget::Regame()
{
    musictype = 2; mymusic->chose(musictype);//切换到1 游戏音乐
    //删除蛇蛇的全部结点
    mysnake.DelAll();

    //初始化分数和关卡
    Sorce = 0;
    life = 3;
    Level = 1;

    //杂七杂八的初始化
    press = false;
    life = 3 ;
    applindex = 0;
    fangxiang = 2;
    GetWord();
    word_dangqian = 0;//初始单词的下标
    word = MyWord[Level-1][word_dangqian].word;
    QFont font("Microsoft YaHei",14);//设置字体
    GameStop = false;//游戏没有停止
    Speed = 100;//设置初始速度

    //开始定时
    timer = new QTimer;
    timer->start(Speed);
    connect(timer,&QTimer::timeout,[&](){SnakeMove();update();});

    //设置最开始的蛇的坐标
    mysnake.head->x = 1;mysnake.head->y = 0;
    Body body;body.x = 0,body.y = 0;
    mysnake.InsertHead(body);

    //初始化地图
    memset(Map,0,16*25*sizeof(int));
    Map[0][0] = -1;//身子
    Map[0][1] = -1;//脑袋
    SetApple(word);//苹果
}

void Widget::Speed_Fast(bool pan)
{
    if(pan==true)
    {Speed = 100;timer->start(Speed);}
}
void Widget::Speed_Midu(bool pan)
{
    if(pan==true)
    {Speed = 300;timer->start(Speed);}
}
void Widget::Speed_Slow(bool pan)
{
    if(pan==true)
    {Speed = 500;timer->start(Speed);}
}

//重新开始
void Widget::Rebegin()
{
    musictype = 2; mymusic->chose(musictype);//切换到1 游戏音乐
    GameStop = true;
    memset(Map,0,16*25*sizeof(int));
    Body* work = mysnake.head;

    //重新分布蛇的位置
    while (work)
    {
       int x = work->x,y = work->y;
       Map[y][x]=-1;
       work = work->next;
    }
}

//放苹果
void Widget::SetApple(string word)
{
    memset(vis,0,15);
    applindex = 0;//每次调用这个函数就说明是个新单词 要初始化最开始的下标
    int x = mysnake.head->x  ,y = mysnake.head->y  ;
    applmax = word.length();
    for(int i = 0,len = word.length();i<len;i++)
    {
        while(Map[y][x]!=0 || (y==mysnake.head->y || x==mysnake.head->x))
        {
            y = RangedRandDemo(0,16-1);
            x = RangedRandDemo(0,25-1);
        }
        Map[y][x] = word[i]-'a'+1;
        AllApple[i].x = x;
        AllApple[i].y = y;
        AllApple[i].cha = word[i]-'a'+1;
    }
}

//画画
void Widget::paintEvent(QPaintEvent *event)
{
    //更新得分
    ui->Sorce->setText(numtoqstr(Sorce));
    ui->Level->setText(numtoqstr(Level));
    ui->Life->setText(numtoqstr(life));
    //设置单词信息
    ui->word->setText(strtoqstr(MyWord[Level-1][word_dangqian].word));
    ui->cixing->setText(strtoqstr(MyWord[Level-1][word_dangqian].type));
    press = false;
    QPainter p(this);
    QPen pen;
    pen.setColor(Qt::white);
    p.setPen(pen);
    for(int i = 0;i<16;i++)
        p.drawLine(20,20+40*i,24*40+20,20+40*i);

    for(int i=0;i<25;i++)
        p.drawLine(20+40*i,20,20+40*i,15*40+20);

    pen.setColor(Qt::blue);
    p.setPen(pen);
    //画蛇的身子
    Body* work = mysnake.head;
    //先画脑袋
    p.drawPixmap(20+40*work->x,20+40*work->y,40,40,QPixmap(StrHead));
    //再画身子
    work = work->next;
    while (work)
    {
        p.drawPixmap(20+40*work->x,20+40*work->y,40,40,QPixmap(StrBody));
        work = work->next;
    }

    //画苹果
    for(int i=0;i<applmax;i++)
    {
        //只有未被吃的苹果才能画出来
        if(vis[i]==false)
           p.drawPixmap(20+(AllApple[i].x)*40,20+(AllApple[i].y)*40,40,40,QPixmap(StrAppleImage[AllApple[i].cha]));
    }
    for(int i= 0 ;i<16;i++)
        for(int k = 0;k<25;k++)
            if(Map[i][k]<0)
            {
                p.drawText(20+k*40,20+i*40,40,40,Qt::AlignCenter, QString("-1"));
            }
}

//向上移动
bool Widget::MoveUp(int x,int y)
{
    if(y-1>=0 && Map[y-1][x]>=0)//这样就说明死不了
    {
        //当没有碰到吃的
        if(Map[y-1][x]==0)
       {
            //移动身子 脑袋结点坐标变化
            Map[mysnake.end->y  ][mysnake.end->x  ] = 0;
            mysnake.Move();
            mysnake.head->y-=1;
            Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
        }
        else
        {
            //两种情况 按照顺序和没有按照顺序
            //按照顺序吃的
            if(Map[y-1][x]==AllApple[applindex].cha)
            {
                Sorce+=10*Level;
                qDebug()<<"按照顺序吃的"<<applindex;
                mysnake.Eat();
                mysnake.head->y-=1;
                Map[mysnake.head->y  ][mysnake.head->x  ] = -1;


                for(int i = 0;i<applmax;i++)//每次都要从0开始查，不然会出现漏的情况
                {
                    if(AllApple[i].x==x&&AllApple[i].y == y-1)
                       { vis[i]=1;    break;}
                }
                 applindex++;//单词的下标加一
                 if(applindex==applmax)//当整个单词都拼对的时候 额外加分
                     {
                     Sorce+=50; word_dangqian++;
                     if(Sorce>(2*Level-1)*200)
                     {
                         Level++;
                         word_dangqian = 0;
                     }

                     word = MyWord[Level-1][word_dangqian].word;
                     SetApple(word);
                 }

            }
            //没按照顺序
            else
             return false;
        }
    }
    else //死啦
      {qDebug()<<"Zhuang Die"; return false;}

    return true;
}

//向下移动
bool Widget::MoveDown(int x,int y)
{
    if(y+1<16-1 && Map[y+1][x]>=0)//这样就说明死不了
    {
        //当没有碰到吃的
        if(Map[y+1][x]==0)
       {
            //移动身子 脑袋结点坐标变化
            Map[mysnake.end->y  ][mysnake.end->x  ] = 0;
            mysnake.Move();
            mysnake.head->y+=1;
            Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
        }
        else
        {
            //两种情况 按照顺序和没有按照顺序
            //按照顺序吃的
            if(Map[y+1][x]==AllApple[applindex].cha)
            {
                 Sorce+=10*Level;
                qDebug()<<"On Sequence"<<applindex;
                 mysnake.Eat();
                 mysnake.head->y+=1;
                 Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
                for(int i = 0;i<applmax;i++)
                {
                    if(AllApple[i].x==x&&AllApple[i].y == y+1)
                       { vis[i]=1;    break;}
                }
                 applindex++;//单词的下标加一
                 if(applindex==applmax)//当整个单词都拼对的时候 额外加分
                     {
                     Sorce+=50; word_dangqian++;
                     if(Sorce>(2*Level-1)*200)
                     {
                         Level++;
                         word_dangqian = 0;
                     }

                     word = MyWord[Level-1][word_dangqian].word;
                     SetApple(word);
                 }
            }
            //没按照顺序
            else
             {qDebug()<<"没有按照顺序"; return false;}
        }
    }
    else //死啦
       {qDebug()<<"Killed by a collision"; return false;}

    return true;
}

//向左移动
bool Widget::MoveLeft(int x,int y)
{
    if(x-1>=0 && Map[y][x-1]>=0)//这样就说明死不了
    {
        //当没有碰到吃的
        if(Map[y][x-1]==0)
       {
            //移动身子 脑袋结点坐标变化
            Map[mysnake.end->y  ][mysnake.end->x  ] = 0;
            mysnake.Move();
            mysnake.head->x-=1;
            Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
        }
        else
        {
            //两种情况 按照顺序和没有按照顺序
            //按照顺序吃的
            if(Map[y][x-1]==AllApple[applindex].cha)
            {
                 Sorce+=10*Level;
                qDebug()<<"按照顺序吃的"<<applindex+1;
                mysnake.Eat();
                mysnake.head->x-=1;
                Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
                for(int i = 0;i<applmax;i++)
                {
                    if(AllApple[i].x==x-1&&AllApple[i].y == y)
                       { vis[i]=1;    break;}
                }
                 applindex++;//单词的下标加一
                 if(applindex==applmax)//当整个单词都拼对的时候 额外加分
                     {
                     Sorce+=50; word_dangqian++;
                     if(Sorce>(2*Level-1)*200)
                     {
                         Level++;
                         word_dangqian = 0;
                     }

                     word = MyWord[Level-1][word_dangqian].word;
                     SetApple(word);
                 }
            }
            //没按照顺序
            else
             {qDebug()<<"没有按照顺序"; return false;}
        }
    }
    else //死啦
       {qDebug()<<"Killed by a collision"; return false;}

    return true;
}

//向右移动
bool Widget::MoveRight(int x,int y)
{
    if(x+1<25-1 && Map[y][x+1]>=0)//这样就说明死不了
    {
        //当没有碰到吃的
        if(Map[y][x+1]==0)
       {
            //移动身子 脑袋结点坐标变化
            Map[mysnake.end->y  ][mysnake.end->x  ] = 0;
            mysnake.Move();
            mysnake.head->x+=1;
            Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
        }
        else
        {
            //两种情况 按照顺序和没有按照顺序
            //按照顺序吃的
            if(Map[y][x+1]==AllApple[applindex].cha)
            {
                 Sorce+=10*Level;
                qDebug()<<"按照顺序吃的"<<applindex;
                mysnake.Eat();
                mysnake.head->x+=1;
                Map[mysnake.head->y  ][mysnake.head->x  ] = -1;
                for(int i = 0;i<applmax;i++)
                {
                    if(AllApple[i].x==x+1&&AllApple[i].y == y)
                       { vis[i]=1;    break;}
                }
                 applindex++;//单词的下标加一
                 if(applindex==applmax)//当整个单词都拼对的时候 额外加分
                     {
                     Sorce+=50; word_dangqian++;
                     if(Sorce>(2*Level-1)*200)
                     {
                         Level++;
                         word_dangqian = 0;
                     }

                     word = MyWord[Level-1][word_dangqian].word;
                     SetApple(word);
                 }
            }
            //没按照顺序
            else
             {qDebug()<<"没有按照顺序"; return false;}
        }
    }
    else //死啦
       {qDebug()<<"Killed by a collisionr"; return false;}

    return true;
}

//摁键
void Widget::keyPressEvent(QKeyEvent *event)
{

    if(press==false)
    {
    //向上移动
    if(event->key()==Qt::Key_W&&(fangxiang!=2||jiejin))
   {
        if(jiejin&&fangxiang==2)
            return ;
        jiejin = false;
        if(GameStop == true)
        {
            GameStop = false;
            emit GameStart();
        }
        press = true;
        //qDebug()<<"↑";
        fangxiang = 1;
    }
    //向下移动
    if(event->key()==Qt::Key_S&&(fangxiang!=1||jiejin))
    {
        if(jiejin&&fangxiang==1)
            return ;
        if(GameStop == true)
        {
            jiejin = false;
            GameStop = false;
            emit GameStart();
        }
        press = true;
       // qDebug()<<"↓";
        fangxiang = 2;
    }
    //向左移动
    if(event->key()==Qt::Key_A&&(fangxiang!=4||jiejin))
    {
        if(jiejin&&fangxiang==4)
            return ;
        if(GameStop == true)
        {
            jiejin = false;
            GameStop = false;
            emit GameStart();
        }
        press = true;
        //qDebug()<<"←";
        fangxiang = 3;
     }
    //向右移动
    if(event->key()==Qt::Key_D&&(fangxiang!=3||jiejin))
    {
        if(jiejin&&fangxiang==3)
            return ;
        if(GameStop == true)
        {
            jiejin = false;
            GameStop = false;
            emit GameStart();
        }
        press = true;
        //qDebug()<<"→";
        fangxiang = 4;
    }

    }

}

//蛇的移动
void Widget::SnakeMove()
{
    int x = mysnake.head->x,y = mysnake.head->y;
    switch (fangxiang) {
    case 1://向上移动
        if(MoveUp(x,y)==false)//如果死了
        {
            if(life==0)//如果已经没有剩余生命了
                emit DIED_end();
            else
            {jiejin = true;emit DIED_life();}
        }
        break;
    case 2://向下移动
        if(MoveDown(x,y)==false)//如果死了
        {
            if(life==0)//如果已经没有剩余生命了
                emit DIED_end();
            else
            {jiejin = true;emit DIED_life();}
        }
        break;
    case 3://向左移动
        if(MoveLeft(x,y)==false)//如果死了
        {
            if(life==0)//如果已经没有剩余生命了
                emit DIED_end();
            else
            {jiejin = true;emit DIED_life();}
        }
        break;
    case 4://向右移动
        if(MoveRight(x,y)==false)//如果死了
        {
            if(life==0)//如果已经没有剩余生命了
                emit DIED_end();
            else
            {jiejin = true;emit DIED_life();}
        }
        break;
    default:
        break;
    }
}

//析构函数
Widget::~Widget()
{
    delete ui;
}

void Widget::GetWord()
{

    WORD Word[1000];
    int index = 0;
    string mid = "";

    QFile file(QString("image/英语四级高频词汇700个.txt"));
    if(!file.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        qDebug()<<"Can't open the file!"<<endl;
    }
    while(!file.atEnd())
    {
        QByteArray line = file.readLine();
        QTextCodec *tc = QTextCodec::codecForName("GBK");
        QString str = tc->toUnicode(line);
        str.toLocal8Bit();

        mid = str.toStdString();

        if (mid.length() < 5)
            continue;
        unsigned int i = 0;
        while (mid[i]<97 || mid[i]>'z')
                    i++;
                while (mid[i] != ' '&&mid[i]>0)
                {
                    Word[index].word += mid[i];
                    i++;
                }
                while(mid[i]==' ')
                    i++;
                while (i<mid.length())
                {
                    Word[index].type += mid[i];
                    i ++ ;
                }
                index++;
    }
        sort(Word, Word + index, cmp);
        int kk = 0;
        int i=0;
        int j=0;
        //第一档
        while(Word[i].word.length()<=3)
        {
            MyWord[kk][j] = Word[i];
            j++;i++;
        }
        kk++;
        j=0;
        //第二档
        while(Word[i].word.length()<=5)
        {
            MyWord[kk][j] = Word[i];
               j++;i++;
        }
        kk++;
        j=0;
        //第三档
        while(Word[i].word.length()<=7)
        {
            MyWord[kk][j] = Word[i];
               j++;i++;
        }
        kk++;
        j=0;
        //第四档
        while(Word[i].word.length()<=9)
        {
            MyWord[kk][j] = Word[i];
               j++;i++;
        }
        kk++;
        j=0;
        //第5档
        while(i<index)
        {
            MyWord[kk][j] = Word[i];
            j++;i++;
        }
}

