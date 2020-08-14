## back-end(后端部分)

[![前端代码库](https://img.shields.io/badge/前端-王相杰-91d5ff)](https://github.com/Asa-kura/note)[![后端代码仓库](https://img.shields.io/badge/后端-董安宁-1890ff)](https://github.com/UncoDong/back-end)[![算法代码仓库](https://img.shields.io/badge/算法-张淇金-2f54eb)](https://github.com/UncoDong/Music-Attention-pytorch-onlycode)[![测试代码仓库](https://img.shields.io/badge/测试-董安宁-061178)](https://github.com/UncoDong/TAPD-test)

### 接口设计

#### MusicBackEnd

主工程，用来链接所有Myapp打头的子工程

- /Myapp_runweb 					 页面展示
- /Myapp_covert2musicscore  转换成曲谱的算法
- /Myapp_dealfile                      文件相关处理
- /Myapp_login                           登录相关处理

##### Myaoo_runweb

页面展示相关的功能，用来将html网页返回给用户。所有的JSP文件和CSS文件都保存在这里。

- /Myapp_runweb/home 						 主页
- /Myapp_runweb/str2musicscore 		在线字符转换
- /Myapp_runweb/wavescope 		       波形图
- /Myapp_runweb/pianoOnLine 		   在线钢琴
- /Myapp_runweb/metronome 		    节拍器
- /Myapp_runweb/file2musicscore  在线文件转换

##### Myapp_convert2musicscore

核心算法工程，提供**字符串转换乐谱**和**音频文件转换乐谱**的功能函数。生成的**MusicXML**，**MID文件**也都保存在这里。

- /Myapp_convert2musicscore/uploadstr            上传字符串
- /Myapp_convert2musicscore/changestr2pic     将字符串转换成pic

##### Myapp_dealfile

处理文件相关的工程。用来实现文件的**上传**和**下载**功能。以及调用Myapp_convert2musicscore中的转换函数对文件进行处理。

- /Myapp_dealfile/downloadfile/\<str:filename\>        下载文件
- /Myapp_dealfile/uploadfile                                        上传文件
- /Myapp_dealfile/dealfile                                             将文件处理成曲谱相关

##### Myapp_login

登录功能相关的工程。用来实现用户的**登录**，**登出**，**保持登陆状态**，**注册**等功能。





### 数据库设计

##### User

用来存储用户的登录信息，如用户名和密码

| 序号 | 名称     | 描述   | 类型      | 键   | 备注              |
| ---- | -------- | ------ | --------- | ---- | ----------------- |
| 1    | id       | 表主键 | AutoField | 主键 |                   |
| 2    | name     | 用户名 | CharField | 外键 | 纯英文+数字的组合 |
| 3    | password | 密码   | CharField |      | 纯英文+数字的组合 |

##### Score

用来存储用户保存的曲谱信息和wav信息，主要是保存路径

| 序号 | 名称       | 描述             | 类型      | 键   | 备注       |
| ---- | ---------- | ---------------- | --------- | ---- | ---------- |
| 1    | id         | 表主键           | AutoField | 主键 |            |
| 2    | user_name  | 用户名           | CharField |      | 不得为中文 |
| 3    | png_path   | 曲谱图片路径     | CharField |      |            |
| 4    | wav_path   | 曲谱wav文件路径  | CharField |      |            |
| 5    | json_path  | 曲谱json文件路径 | CharField |      |            |
| 6    | score_name | 曲谱的标题       | CharField |      |            |

