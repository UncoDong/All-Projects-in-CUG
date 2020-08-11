# :atm:Three-Tier Architecture

将整个业务划分为“表现层”，“业务逻辑层”，“数据访问层”，以体现**高内聚低耦合**的思想。

Dividing the business into "Client Tire", "Business Logic Tier" and "Database Tier", in order to realize the idea of **Low Coupling, High Cohesion**



本次实习中，我在本地计算机搭建表现层，EC2远程服务器搭建业务逻辑层，AWS远程数据库搭建数据访问层。采用混合编程的思想，使用jdbc连接数据库，在EC2部署python程序调用jar包访问数据库，并通过SQS消息队列返回到本地计算机。

In this project, Client Tire was set in my local laptop, Business Logic Tier was set in EC2, Database Tier was set in the AWS's MySQL database. Mixturing Python and Java, I used jdbc to connect DB, and parcel it into a jar which will be used by python in EC2 to exchange the data. Finally, all the result from  Business Logic Tier will be transmit to laptop by SQS.

## 成果展示(The Accomplishment)

![image-20200811091442102](pics/image-20200811091442102.png)

<center>Architecture Design </center>

![image-20200811092529551](pics/image-20200811092529551.png)

<center>Interface Design</center>

![image-20200811092631527](pics/image-20200811092631527.png)

<center>Interfaces Encapsulating by Python (Database Tier)</center>

![image-20200811093011254](pics/image-20200811093011254.png)

<center>Test for Connect Through SQS (Business Logic Tier)</center>

![image-20200811093058067](pics/image-20200811093058067.png)

<center>Localhost Result (Client Tire)</center>

![image-20200811093755047](pics/image-20200811093755047.png)

<center>Three Tire</center>

## 参考(Reference)

- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
- https://docs.aws.amazon.com/sqs/index.html#lang/zh_cn
- https://docs.aws.amazon.com/sns/index.html#lang/zh_cn4
- https://blog.csdn.net/weixin_39407066/article/details/83625316
- https://www.cnblogs.com/ai594ai/p/8615818.html

