P81
# 理解RabbitMQ日志
### 在文件系统中读日志
* LOG_BASE，默认值，在rabbitmq-server脚本显示如下: LOG_BASE=/var/log/rabbitmq
* 两个日志文件:RABBITMQ_NODENAME-sasl.log和RABBIMQ_NODENAME.log。
  其中这里的RABBITMQ_NODENAME指的是_rabbit@localhost_或者说就是rabbit，这取决于你如何配置系统。
* sasl日志和另一个日志有什么区别呢？SASL(System Application Support Libraries，系统应用程序支持库)是库的集合
* 当RabbitMQ记录Erlang相关信息时，它会将日志写入rabbit-sasl.log文件。（如Erlang的崩溃报告,调试无法启动的RabbitMQ）
```
=INFO REPORT==== 10-Sep
accepted TCP connection on 0.0.0.0:5672 from 192.168.1.253:44550

```
这段信息对调试你的消费者/生产者很有帮助;你可以看到它们是否连接正常，连接是否突然中断，等等.
从rabbit.log文件你还能看到像对用户、交换器、队列等的操作事件

### 轮换日志
* 首先你需要知道服务器是否启动，它会重新创建日志文件并在旧文件后面添加一个数字。rabbit.log.1这样的文件.
* 如果你想手动轮换日志文件或者通过cronjob来达成的话，则可以使用--rabbitmqctl
```
./rabbitmqctl rotate_logs suffix
```

### 通过AMQP实时访问日志


### Mnesia和主机名
* 先要启动Mnesia数据库(nosql)
* 导致Mnesia启动失败的原因大致有二。
>> * 第一个也是最常见的是MNESIA_BASE目录的权限问题.
>> * 如果主机名更改了，或集群模式下，无法在启动的时候连接到其它节点，报读取表格失败。

P92
# 异步状态思维(分离请求和运作)
### 提供扩展性:没有负载均衡器的世界
* 使用消息通信最大的好处之一是，为应用增加处理能力变得简单。
>> * 通过增加10台新的dog_wallk_process服务器增加了10倍的处理能力。


### 发后即忘模型
* 消息通信适用的主要领域之一是发后即忘的处理模式。
### 私有队列和发送确认
* 由于AMQP消息是单向的，RPC服务器如何才能将结果返回给原始客户端呢?由于RabbitMq处于中间环节，
  RPC服务器甚至都不知道客户端调用者的身份(除非特定ID).
* rabbitmq团队想出了一个优雅的解决方案：使用消息来发回应答。在每个AMQP消息头里有个字段叫作reply_to.
  消息的生产都可以通过该字段来确定队列名称，并监听队列等待应答。收接收消息的RPC服务应答，并以队列名称作为路由键。

### 使用reply_to来实现简单的JSON RPC










