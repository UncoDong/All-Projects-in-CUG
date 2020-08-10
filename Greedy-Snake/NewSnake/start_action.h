#ifndef START_ACTION_H
#define START_ACTION_H

#include <QWidget>
#include<QPainter>
#include<QPen>
#include<QBrush>
#include<QTimerEvent>
#include<QDebug>
#include<QLabel>
#include<QPixmap>//也是加图片用的
#include"mybutton.h"
class Start_Action : public QWidget
{
    Q_OBJECT
    int num[30][13];
    int full;
    int timerID;

    int mi;
    int my;
    int timeshark;
    bool shark,pan;
    bool showb;

    MyButton c;
    QLabel w;


public:
    explicit Start_Action(QWidget *parent = nullptr);

protected:
    void paintEvent(QPaintEvent *event);
    void timerEvent(QTimerEvent *event);

signals:
    void show_button();
    void START();//开始！
    void beginstartmusic();//放开场音乐

public slots:
};

#endif // START_ACTION_H
