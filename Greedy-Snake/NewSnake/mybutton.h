#ifndef MYBUTTON_H
#define MYBUTTON_H

#include <QPushButton>
#include<QWidget>
class MyButton : public QPushButton
{
    Q_OBJECT
public:
    explicit MyButton(QWidget *parent = nullptr);
    ~MyButton();
protected:
    void enterEvent(QEvent *event);//重写鼠标进入事件
    void leaveEvent(QEvent *event);//重写鼠标离开事件
    void mousePressEvent(QMouseEvent *e);//重写鼠标点击事件

signals:
    void StartGame();
public slots:
};

#endif // MYBUTTON_H
