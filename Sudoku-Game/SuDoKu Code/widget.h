#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include<QPainter>
#include<QPen>
#include<QDebug>
#include<QMouseEvent>
#include<QString>
#include<QFont>
#include<vector>
#include<QKeyEvent>
#include<QMessageBox>
#include"music.h"
#include<fstream>
#include<string>
#include<QTimer>
#include"solvesudoku.h"
using namespace std;
namespace Ui {
class Widget;
}
struct SDKNode
{
    int x=-1;int y=-1;
};
struct RepealNode
{
    int x=-1;int y=-1;
    char now;//当前字符
    char his;//历史字符
};
class Widget : public QWidget
{
    Q_OBJECT
public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();
    void Delmusic();         //关闭音乐
    bool Check(int x,int y); //检查是否为不能删掉的
    void SaveInBlack(); //放入不能被删掉的黑色数字
    bool Submit();      //提交 判断是否正确
    void RepealLeft();  //向左撤销
    void RepealRight(); //向右撤销
    bool Deal();        //数独得解
    void ReadSQL();     //获得数独
    void Harder();      //难度增加
    void Easyer();      //难度降低
    void Clean();       //清空棋盘
    void MakeAns();     //得到结果
    void TimeOut();     //计时结束
    void TimeStop();    //暂停计时
    void TimeReStart(); //继续计时
private:

    Ui::Widget *ui;
    char input;              //用户输入
    vector<RepealNode> RepealStack;//撤销的栈
    int SIndex;              //StackIndexBegin 起始位置
    vector<SDKNode>BlackWord;//不能被删掉的黑色数字
    SDKNode WrongWord;//遍历的时候错误的数组
    vector<vector<char> >SDKMap;//给用户看的数组
    vector<vector<char> >ANS; //算法得到的正确结果
    SDKNode ChooseNode;       //被选中的结点
    Music *mymusic;           //音乐线程
    QThread *music_thread;    //音乐的子线程
    int W_and_B;              //黑白数字的总数
    vector<vector<vector<char>>>SQL;//数独库
    int HardIndex;            //难度的等级
    int SmallHardIndex;       //小的难度的登记
    QTimer* timer;            //计时器
    int myclock;              //我的表
    bool STOP;                //停止计时
protected:
    void paintEvent(QPaintEvent *event);
    void mousePressEvent(QMouseEvent *event);
    void keyPressEvent(QKeyEvent *event);
};

#endif // WIDGET_H
