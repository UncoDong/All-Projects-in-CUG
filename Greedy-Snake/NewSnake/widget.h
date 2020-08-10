#ifndef WIDGET_H
#define WIDGET_H
#include<QPainter>   //画家
#include<QPen>       //画笔
#include<QBrush>     //笔刷
#include <QWidget>
#include<QPaintEvent>//画画
#include<QTimer>    //计时器
#include<QKeyEvent> //摁键
#include<QDebug>    //debug 用来输出东西的
#include<string>    //字符串
#include<QPushButton>//摁钮
#include<QLabel>    //Label类
#include<QFont>     //字体
#include<QPixmap>   //插图
#include<QString>   //Q字符串
#include<sstream>   //数字转换字符串
#include<QFile>     //文件流
#include<QTextCodec>//文件中文字的处理
#include<QThread>

#include"music.h"  //背景音乐
#include"snake.h"  //蛇蛇
#include"start_action.h"//开场动画
using namespace std;
//存放苹果信息的结点
struct EachApple
{
    int x,y;
    int cha;
};
//存放单词信息的结点
struct WORD
{
    string word="";//单词
    string type="";//词性

};


namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    void SetApple(string word);//安放苹果
    bool MoveUp(int x,int y);//向上移动
    bool MoveDown(int x,int y);//向下移动
    bool MoveLeft(int x,int y);//向左移动
    bool MoveRight(int x,int y);//向右移动
    void SnakeMove();     //蛇的移动
    void Rebegin();       //重新开始一条命
    void Regame();        //重新开始游戏
    void GetWord();       //读取单词
    void Speed_Fast(bool pan);    //变快速
    void Speed_Midu(bool pan);    //变中速
    void Speed_Slow(bool pan);    //变慢速
    void Delmusic();              //关闭音乐
    ~Widget();

protected:
    void paintEvent(QPaintEvent *event);
    void keyPressEvent(QKeyEvent *event);
private:
    Ui::Widget *ui;
    QTimer *timer;
    Snake mysnake;
    int Map[16][25];
    bool press;//防止回头撞
    string word;//单词
    EachApple AllApple[15];//用来存放每个apple的信息的
    bool vis[15];     //是否被访问
    int applmax;     //单词的最长长度
    int applindex;   //用来检查有没有按照顺序吃
    int fangxiang;   //方向 1向上 2向下 3向左 4向右
    QString StrAppleImage[27];//苹果图片地址
    QString StrHead;//蛇头图片
    QString StrBody;//蛇身图片
    bool GameStop;  //游戏暂停
    int Speed;      //速度
    WORD MyWord[5][300];//存放单词用的
    int word_dangqian;       //当前单词下标
    int Sorce;//游戏得分
    int Level;//游戏等级(难度)
    int life;  //生命
    bool jiejin;//解禁不能回头的
    int musictype;  //背景音乐类型    1 开场 2 背景 3 死亡 4 减一
    Music *mymusic; //音乐线程
    QThread *music_thread;    //音乐的子线程
    Start_Action a; //开场动画
signals:
    void DIED_life();//减少一条生命的死亡
    void DIED_end();//命用完了的死亡
    void GameStart();//开始游戏
};

#endif // WIDGET_H
