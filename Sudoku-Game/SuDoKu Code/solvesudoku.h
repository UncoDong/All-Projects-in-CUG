#ifndef SOLVESUDOKU_H
#define SOLVESUDOKU_H
#include<string>
#include<vector>
using namespace std;
class Solution
{
    struct DanceNode
    {
        DanceNode* right = NULL;//右边
        DanceNode* left = NULL; //左边
        DanceNode* up = NULL;	//上面
        DanceNode* down = NULL; //下面
        int *col = NULL;               //方便改bug
        int *row = NULL;               //方便改bug
        int *num = NULL;               //方便改bug
    };

    DanceNode***DanceMatrix;//舞蹈链的数组
    DanceNode**DanceHead;   //舞蹈链的列索引
    DanceNode**DanceHang;   //舞蹈链的行索引
    DanceNode* head;        //列索引的头
public:
    void Begin()
    {
        head = new DanceNode;
        DanceHead = new DanceNode *[4 * 9 * 9];
        for (int i = 0; i < 4 * 9 * 9; i++)
        {
            DanceHead[i] = new DanceNode;
            DanceHead[i]->num = new int(0);
            if (i > 0)
            {
                DanceHead[i - 1]->right = DanceHead[i];
                DanceHead[i]->left = DanceHead[i - 1];
            }
        }
        head->right = DanceHead[0];
        DanceHead[0]->left = head;
        DanceHead[4 * 9 * 9 - 1]->right = head;
        head->left = DanceHead[4 * 9 * 9 - 1];
        DanceHang = new DanceNode *[9 * 9 * 9];
        for (int i = 0; i < 9 * 9 * 9; i++)
        {
            DanceHang[i] = new DanceNode;
            DanceHang[i]->row = new int(i);
        }
        DanceMatrix = new DanceNode**[9 * 9 * 9];
        for (int i = 0; i < 9 * 9 * 9; i++)
        {
            DanceMatrix[i] = new DanceNode*[4 * 9 * 9];
            for (int j = 0; j < 4 * 9 * 9; j++)
                DanceMatrix[i][j] = nullptr;
        }
        //进行初始化
        int row = 0, col = 0, num = 0, gong = 0;
        DanceNode *work1, *work2, *work3, *work4;
        for (int i = 0; i < 9 * 9 * 9; ++i)
        {
            row = i / 81;
            col = (i - row * 81) / 9;
            num = i - (row * 81 + col * 9);
            gong = (int(row / 3) * 3 + int(col / 3));
            //1
            DanceMatrix[i][row * 9 + col] = new DanceNode;
            work1 = DanceMatrix[i][row * 9 + col];
            work1->up = DanceHead[row * 9 + col];
            work1->row = new int(row);
            work1->col = new int(col);
            work1->num = new int(num);
            //2
            DanceMatrix[i][81 + 9 * col + num] = new DanceNode;
            work2 = DanceMatrix[i][81 + 9 * col + num];
            work2->up = DanceHead[81 + 9 * col + num];
            work2->row = new int(row);
            work2->col = new int(col);
            work2->num = new int(num);
            //3
            DanceMatrix[i][162 + 9 * row + num] = new DanceNode;
            work3 = DanceMatrix[i][162 + 9 * row + num];
            work3->up = DanceHead[162 + 9 * row + num];
            work3->row = new int(row);
            work3->col = new int(col);
            work3->num = new int(num);
            //4
            DanceMatrix[i][243 + 9 * gong + num] = new DanceNode;
            work4 = DanceMatrix[i][243 + 9 * gong + num];
            work4->up = DanceHead[243 + 9 * gong + num];
            work4->row = new int(row);
            work4->col = new int(col);
            work4->num = new int(num);
            //行连接
            //1
            DanceHang[i]->right = work1;
            work1->left = DanceHang[i];
            work1->right = work2;
            //2
            work2->left = work1;
            work2->right = work3;
            //3
            work3->left = work2;
            work3->right = work4;
            //4
            work4->left = work3;
            work4->right = DanceHang[i];
            DanceHang[i]->left = work4;
        }
        DanceNode*work;
        int index = 0;
        int cal = 0;
        for (int i = 0; i < 9 * 9 * 4; i++)
        {
            work = DanceHead[i];
            index = 0;
            cal = 0;
            while (index < 9 * 9 * 9)
            {
                if (DanceMatrix[index][i] != nullptr)
                {
                    work->down = DanceMatrix[index][i];
                    work = DanceMatrix[index][i];
                    cal++;
                }
                index++;
            }
            work->down = DanceHead[i];
            *(DanceHead[i]->num) = cal;
        }
    }

    //改变列索引头
    void change(int row, int col, int num, vector<vector<char>>& board)
    {
        int index = row * 81 + col * 9 + num;
        //把该列的左右两边连起来
        DanceNode* node = DanceHang[index];
        node = node->right;
        while (node != DanceHang[index])
        {
            node->up->left->right = node->up->right;//左边和右边链接
            node->up->right->left = node->up->left;//右边和左边链接
            node = node->right;
        }
    }

    //改变列索引头
    bool change(DanceNode* work, vector<vector<char>>& board)
    {
        DanceNode*node = work;

        bool pan = true;//判断是否被改变了
        while (node != work->left)
        {
            if (node->up->left->right != node->up)
            {
                pan = false; break;
            }
            node = node->right;
        }
        node = work;
        if (pan)
        {
            while (node != (work->left))
            {
                node->up->left->right = node->up->right;//左边和右边链接
                node->up->right->left = node->up->left;//右边和左边链接
                node = node->right;
            }
            int row = *(node->right->row);
            int col = *(node->right->col);
            int num = *(node->right->num);
            //cout << row << ends << col << ends << num << ends << endl;
            board[row][col] = '1' + num;
        }
        return pan;
    }

    //改回来
    void changeback(DanceNode* work, vector<vector<char>>& board)
    {
        DanceNode*node = work;
        while (node != (work->left))
        {
            node->up->left->right = node->up;
            node->up->right->left = node->up;
            node = node->right;
        }
        int row = *(node->right->row);
        int col = *(node->right->col);
        board[row][col] = '.';
    }

    //深度遍历
    bool dfs(vector<vector<char>>& board)
    {
        if (head->right == head)return true;
        int max = 9;
        DanceNode*find = head->right;
        DanceNode* node = find->down;
        while (find != head)
        {
            if (*(find->num) < max)
            {
                node = find->down;
                max = *(find->num);
            }
            find = find->right;
        }

        while (node->up)
        {
            if (change(node, board))
            {
                if (dfs(board))
                    return true;
                changeback(node, board);
            }
            node = node->down;
        }
        return false;
    }
    //解数独函数
    bool solveSudoku(vector<vector<char>>& board)
    {
        Begin();
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                if (board[i][j] != '.')
                    change(i, j, board[i][j] - '1', board);
        return dfs(board);
        //cout << dfs(board) << endl;
    }
};
#endif // SOLVESUDOKU_H
