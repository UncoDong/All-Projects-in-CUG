#ifndef SNAKE_H
#define SNAKE_H
#include<iostream>
using namespace std;
struct Body
{
    int x = 0;
    int y = 0;
    Body*next = NULL;
    Body*pre  = NULL;
    Body(){}
};
class Snake
{

public:
    Snake();
    void InsertHead(Body body);//头插法增长
    void Move();  //普通移动
    void Eat();   //吃东西的移动
    void DelAll();//删除全部身子
    Body *head;
    Body* end;
    ~Snake();
};

#endif // SNAKE_H
