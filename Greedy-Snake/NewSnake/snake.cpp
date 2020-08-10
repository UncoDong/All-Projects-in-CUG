#include "snake.h"

//构造函数
Snake::Snake()
{
    head = new Body;
    end = head;
}

//头插法增长身子
void Snake::InsertHead(Body body)
{
    Body* work = new Body;
    work->x = body.x;work->y = body.y;
    work->next = head->next;
    head->next = work;
    work->pre = head;
    if(work->next)//如果work的下一个不是空的话
        work->next->pre = work;
    else          //否则表示这是第一个插入的结点 尾结点要指向这个结点
        end = work;

}

//普通移动
void Snake::Move()
{
    //普通移动
    //第一种情况 只有脑袋和一个身子结点
    if(head->next == end)
     {
      end->x = head->x;end->y = head->y;
     }
    //第二种情况 身子结点个数大于一个 把身子的最后一节删掉，放到脑袋后面
    else
    {
        Body *work = end;
        end = end->pre;
        Body save;save.x = head->x;save.y = head->y;
        delete work;
        end->next = NULL;
        InsertHead(save);
    }
    //以上只对身子的结点进行了操作，脑袋(head)的坐标在函数外面随着上下左右移动进行改变
}

//吃东西的移动
void Snake::Eat()
{
    //吃了东西后...其实就是脑袋到了食物的位置，后面的都不动，因此在脑袋后面插入一个脑袋的坐标就可以了
    //好像有点绕？
    Body save;save.x = head->x;save.y = head->y;
    InsertHead(save);
    //脑袋的坐标也是在外面进行改变
}

//删除全部身子
void Snake::DelAll()
{
    Body*work = head;
    while(head->next)
    {
        head = head->next;
        delete work;
        work = head;
    }
    end = head;
    head->next = NULL;
    head->pre = NULL;
}

//析构函数
Snake::~Snake()
{
    DelAll();
    delete head;
}
