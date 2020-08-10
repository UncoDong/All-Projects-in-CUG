

# :snake:Greedy Snake Based on A Star

该贪吃蛇程序使用QT进行UI开发，使用了A*自动寻路算法让蛇自己寻找食物。为了能够尽可能地让贪吃蛇不断变长，并避免死亡，我在传统算法上添加了下面的判断：

- 每次在使用A*判断蛇能够吃到食物后，判断是否会死亡。如果会的话，就向远离食物的方向移动，直到预判吃到食物不死后再去吃。

总共开发时间：一周。在学习QT和调试算法上花费了很多时间。最终结果还是比较满意。



The UI of this game was developed by QT. In order to make the snake find way automatically, I used A star as the algorithm. To avoid death and keep growing, I added the following process to the original algorithm

- Each time when the algorithm find a way to approach the food, it will also judge weather there is a way to escape. If not, the snake will move far away from the food, until it find a way to eat food safety.

I cost a week to finish this program. Most of my time is spent on learning QT and  debug the algorithm



## 成果展示(The Accomplishment)

![image-20200810221645561](C:\Users\UncleDong\AppData\Roaming\Typora\typora-user-images\image-20200810221645561.png)

![image-20200810221856758](C:\Users\UncleDong\AppData\Roaming\Typora\typora-user-images\image-20200810221856758.png)

## 参考(Reference)

- https://www.gamedev.net/reference/articles/article2003.asp