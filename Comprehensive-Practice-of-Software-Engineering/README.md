# :thought_balloon:Comprehensive Practice of Software Engineering

在软件工程综合实习中，我们需要做到

- 使用Scrum敏捷开发
- 确定小组成员角色分配(产品负责人，团队负责人，开发团队)
- 使用TAPD(Tencent Agile Product Development)腾讯敏捷产品研发平台(www.tapd.cn)，完成全生命周期管理
- 使用github作为代码托管平台
- 使用看板布置任务，进行每日进行站立会议，讨论和总结每天的任务
- 项目分成三次迭代，分别为
  - 迭代1：团队组建，前期调研，技术准备
  - 迭代2：开发，回顾
  - 迭代3：需求变更，重构
- 使用Jenkins集成工作环境，要求
  - 使用pytest自动测试
  - 使用SonarQube进行代码质量分析
  - ~~使用Ansible自动发布~~(未能实现)



In this *Comprehensive Practice of Software Engineering*, we need to

- Using Scrum as the method of an agile development process
- Team members grouping as *Product Owner*, *Scrum Master*, *Dev Team*
- Using *TAPD*(Tencent Agile Product Development), a SCRUM platform developed by Tencent, to complete the lifecycle management of the project
- Using *Github* as code hosting platform
- Using board to set mission, using daily stand-up meetings for retrospect
-  Have three Iteration 
  - Iteration ONE：team-creation， pre-research，technological preparations
  - Iteration TWO：develop and review
  - Iteration Three：requirements changes and code restructure
- Using *Jenkins* as continuous integration tool 
  - Using pytest as automated tests
  - Using SonarQube to check the rule of code
  - ~~Using Ansible to publish automaticly~~ (automatic)



## 我们想做什么(What do we wanna do)

听音撰谱系统。想要制作该系统的想法来源于社团活动。我在口琴社中，发现很多人都有自己想要演奏的曲子，但是处于商业机密或者其他原因，很多曲子的谱子资源在网上很少。有一种方法是可以自己扒谱，不过这种方法只适用于乐感好的人。像我这种乐感不好的，只能一点点的试出正确的旋律，非常费时间。因此想能不能制作这么一个系统，可以让用户上传音乐文件后，自动得到谱子，并返回给用户。

We want to make a system which could translate a song to it's musical notation. The idea come from my community activities. When I was in the Harmonica club of my collage, I found many people want to paly their favorite songs by harmonica, but maybe because it is a trade secret or some other reasons, the musical notation tends to be hard to seach in the Internet. Of course we could do it by ourself if our musicality is strong enough. But person like me who is not good at it have to try to get the correct note from keep trying, It always spend a lot of time. So I thought weather I could make such a system which could translate a song into notation in a easy way.  What should a user do is just upload music files and wait for the results.

## 我们要掌握的技术(The technology we need to use)

- 前端 (Front-end)
  - HTML
  - CSS
  - JSP
- 后端 (Back-end)
  - Django
  - SQLite
- 测试 (Test)
  - pytest
  - Jmeter
- 代码质量检测 (Code quality inspection)
  - SonarQube
- 其他要用到的 (Other dependencs)
  - [Music21](http://web.mit.edu/music21/) (For make music)
  - [Pytorch](https://pytorch.org/) (For recurrent neural network)
  - [librosa](https://librosa.org/doc/latest/index.html) (For music analysis)
  - [MuseScore](https://musescore.org/) (For make musical notation)
  - Java (For convert mid to wav)

## 一些图表(Some Graph)

![image-20200814225840968](pics/image-20200814225840968.png)

<center>High level view</center>

![image-20200814105159313](pics/image-20200814105159313.png)

![image-20200814115328682](pics/image-20200814115328682.png)

<center>Activity diagram</center>

![image-20200814115808337](pics/image-20200814115808337.png)

<center>Use case diagram</center>

![技术路线](pics/技术路线.png)

<center>technical routes</center>

![image-20200814120047240](pics/image-20200814120047240.png)

<center>Development routes</center>

![image-20200814120752595](pics/image-20200814120752595.png)



## 开发过程(Development process)

![image-20200814122055513](pics/image-20200814122055513.png)

<center>Number of meeting per day</center>

![image-20200814122243027](pics/image-20200814122243027.png)

<center>Functional Requirement Analysis</center>

![image-20200814122334744](pics/image-20200814122334744.png)

<center>Tools deployment</center>

![image-20200814123321209](pics/image-20200814123321209.png)

![image-20200814123343988](pics/image-20200814123343988.png)

<center>Backlog & Board</center>

![image-20200814123454318](pics/image-20200814123454318.png)

<center>Different Iteration</center>

![image-20200814123753975](pics/image-20200814123753975.png)

<center>Gantt Chart</center>

![image-20200814123947866](pics/image-20200814123947866.png)

![image-20200814123933882](pics/image-20200814123933882.png)

<center>Code Submission Trend (from webhook of GitHub)</center>

![image-20200814124145339](pics/image-20200814124145339.png)

![image-20200814124212206](pics/image-20200814124212206.png)

![image-20200814124221713](pics/image-20200814124221713.png)

![image-20200814124352335](pics/image-20200814124352335.png)

<center>Test Moudle</center>



![image-20200814124527890](pics/image-20200814124527890.png)

![image-20200814124329424](pics/image-20200814124329424.png)

<center>Pipe Line In Jenkins & TAPD</center>

![image-20200814124657141](pics/image-20200814124657141.png)

![image-20200814124726264](pics/image-20200814124726264.png)

<center>Release plan with Burn Down chart</center>

![image-20200814130348078](pics/image-20200814130348078.png)

![image-20200814130238918](pics/image-20200814130238918.png)

<center>Code quality inspection by SonarQube</center>



## 成果展示(The Accomplishment)

![image-20200814130747556](pics/image-20200814130747556.png)

<center>Home Page</center>

![image-20200814130842270](pics/image-20200814130842270.png)

<center>Online Metronome</center>

![image-20200814134653406](pics/image-20200814134653406.png)

<center>Online Piano</center>

![image-20200814134803469](pics/image-20200814134803469.png)

<center>Generate Notation</center>

![image-20200814214013305](pics/image-20200814214013305.png)

<center>User Homepage</center>

![image-20200814214031712](pics/image-20200814214031712.png)

<center>Upload wav for convert</center>



## 代码仓库和博客 (Repositories and Bolgs)

### 代码仓库 (Repositories )

后端仓库 (back-end) 

https://github.com/UncoDong/back-end

前端仓库 (front-end)

https://github.com/Asa-kura/note

算法仓库 (neutral network)

https://github.com/UncoDong/Music-Attention-pytorch-onlycode

测试仓库 (test)

https://github.com/UncoDong/TAPD-test

### 博客 (Bolgs)

TAPD关联Jenkins (Using Jenkins in TAPD)

https://blog.csdn.net/weixin_42763696/article/details/106412881

Tapd GitHub集成 详细图片 (How to connect TAPD with Github)

https://blog.csdn.net/weixin_42763696/article/details/106332665

TAPD pytest自动化测试部署 (git or 本地) (TAPD How to automatically test through pytest)

https://blog.csdn.net/weixin_42763696/article/details/106413263

阿里云服务器 CentOS 7 Tomcat + Jenkins+国内镜像 配置 (Tomcat+Jenkins+Mirror Srouces Published on ECS's Centos 7)

https://blog.csdn.net/weixin_42763696/article/details/106081449

前端学习 HTML基础语法 标签 书写规范 构成 (Learning notes of HTML)

https://blog.csdn.net/ym912305103/article/details/106700143

前端学习笔记 CSS基础布局 样式 书写规范 (Learning notes of CSS)

https://blog.csdn.net/ym912305103/article/details/106700035

前端学习 HTML5和CSS3新特性 高级技巧 JavaScript基础语法  (Learning notes of JavaScript)

https://blog.csdn.net/ym912305103/article/details/106700300
