#include "start_action.h"
#include<QApplication>
Start_Action::Start_Action(QWidget *parent): QWidget(parent)
{

    setWindowTitle("Loading");
    showb=0;
    setFixedSize(1000,500);
    memset(num,0,sizeof(num));
    full=0;
    timerID = this->startTimer(8);

    mi=-1;my=0;shark = 0,pan=0;
    timeshark=0;
    setFixedSize(1000,500);

    //显示图片
    w.setParent(this);
    w.setPixmap(QPixmap("image/字体.png"));
    w.move(0,25);
    w.hide();

    //显示按钮
    c.setParent(this);
    c.move(425,300);
    c.hide();
    //上面这俩显示的，代码换个位置就会出bug，我tm也不知道为什么

    connect(this,&Start_Action::show_button,[&]() { w.show();c.show();});

    connect(&c,&MyButton::StartGame,[&]() { emit START();});

}


void Start_Action::paintEvent(QPaintEvent *event)
{
    if(!shark)
    //创建画刷对象
    {
        QBrush brush;
        brush.setTexture(QPixmap("image/background.jpg"));
        brush.setStyle(Qt::TexturePattern);

        QPainter p(this);
        p.setBrush(brush);

        for(int i=0;i<13;i++)
            for(int j=0;j<30;j++)
            {
                if(num[i][j]==1)
                    p.drawRect(j*50,i*50,50,50);
            }
    }

   else
   {
        QBrush brush;
        brush.setColor(Qt::white);
        QPainter p(this);
        p.setBrush(brush);
        p.drawRect(rect());
   }

}

void Start_Action::timerEvent(QTimerEvent *event)
{

  if(shark==false)
  {
      if(event->timerId()==this->timerID)
     {
        mi++;
        if(mi>20)
        {
            mi=0;my++;
        }
       num[my][mi]=1;
       full++;
       update();

       if(full==13*20+1)
          {
           shark = true;
            emit beginstartmusic();
          }
    }
  }
  else
  {
      if(timeshark<40)
      {
      timeshark++;
      update();
      }
      else
          pan = true;

  }
  if(pan)
  {
      shark = 0;
       update();
       killTimer(this->timerID);
       emit show_button();
  }

}



