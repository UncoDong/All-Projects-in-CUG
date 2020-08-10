#include "mybutton.h"
#include <QPixmap>
#include <QBitmap>
#include<QMouseEvent>
#include<QDebug>
MyButton::MyButton(QWidget *parent) :QPushButton(parent)
{

    QPixmap pixmap("image/灰色按钮.png");
    resize(pixmap.size());
    setMask(QBitmap(pixmap.mask()));
    setStyleSheet("QPushButton{border-image: url(image/灰色按钮.png);}");
}

void MyButton::enterEvent(QEvent *event)
{
    setStyleSheet("QPushButton{border-image: url(image/按钮高亮.png);}");
}
void MyButton::leaveEvent(QEvent *event)
{
     setStyleSheet("QPushButton{border-image: url(image/灰色按钮.png);}");
}
void MyButton::mousePressEvent(QMouseEvent *e)
{
    qDebug()<<"摁下去啦";
    emit StartGame();//发送开始游戏的信号
}
MyButton::~MyButton()
{

}
