

# :triangular_ruler:Sudoku based on Dancing Links

该数独游戏也使用QT进行UI开发，使用了舞蹈链算法。相比传统的DFS算法，舞蹈链算法更适合复杂的情况。

The UI of this game was also developed by QT. Compared with traditional DFS algorithm, the dancing links could adapt more complex games.

## 成果展示(The Accomplishment)

![image-20200810233424499](pics\image-20200810233424499.png)



因为默认是最难的棋盘，因此在点击“显示答案”的时候会计算很久。当然，如果用DFS的话几乎无法算出结果，这是我试验过的。

Because the first game is the hardest, so when you click *显示答案* , it will caculate for a long time. Of course the DFS algorithm will spend much more time then it, I have tested it.

![image-20200810233525303](pics\image-20200810233525303.png)



# How to Play 

首先在SuDokuEXE文件夹中找到SuDoKu.exe。

You can find SuDoKu.exe in *SuDokuEXE* folder.



## The Keyboard

这里没有用到键盘，所有的操作都是用鼠标操作。

I did set keyboard orders, all the operation is based on the mouse.



## Some Key words

因为我这里用的全部都是中文...因此为了方便在界面上寻找，就不翻译成英文了lol

Because I use only chinese to desire my game... As for easy finding, I will not translate it into English in this instruaction LOL



#### Choose the level

![image-20200810234816781](pics\image-20200810234816781.png)

通过这些按键来更换等级

Using those keys to change the hard level

- 休闲：easy
- 普通：normal
- 中等：middle
- 困难：hard
- 爆裂：the hardest
- 易：decrease the level
- 难：increase the level



### Restart

![image-20200810234836731](pics\image-20200810234836731.png)

清空界面，重新开始游戏

Restart the game



### Submit the answer

![image-20200810234926780](pics\image-20200810234926780.png)

提交答案，会判断当前提交是否正确

Submit the answer and the algoritm will judge weather you win

### Show the answer

使用舞蹈链算法得到答案

Using dance likns to get the answer.

![image-20200810233525303](pics\image-20200810233525303.png)



### Forward and backward

和ctrl+z, ctrl+y一样的功能

Just like ctrl+z and ctrl+y