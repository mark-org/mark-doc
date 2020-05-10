

三、properties配置文件

* canal.properties(系统根配置文件)
* instance.properties(instance级别的配置文件，每个instance一份)

### cannal.properties介绍
1. instance列表定义（列表当前server上有多少个instnace,每个instance的加载方式是spring/manager等）
* cannal.destinations 当前server上部署的instance列表
* canal.conf.dir
// # auto scan instance dir add/remove and start/stop instance
* canal.auto.scan.interval instance自动扫描的间隔时间，单位秒 5
...
2. common参数，将instance.properties的公用参数，抽取放置到这里，这样每个instance启动的时候就可以共享
instance.properties配置定义优先级高于canal.properties
* canal.id 暂无实际意义
* canal.ip 默认本机ip
* canal.port canal server提供socket服务的端口 11111
* canal.file.data.dir canal持久化数据到file上的目录 ./conf(默认和instance.properties为同一目录)

### instance.properties
// # mysql serverId , v1.0.26+ will autoGen
cannal.instance.mysql.slaveId mysql集群配置中serverId 默认1234
// show variables like 'server_id';
https://blog.csdn.net/u012758088/article/details/78789616?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-5&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-5

# canal指定binlog文件和position开始读取
1.查看master mysql binlog:
2.查看该binlog event position;
3.修改conf/${instance}/meta.dat

https://blog.csdn.net/lzhcoder/article/details/90239102
Canal会导致消息重复吗？
答：会，这从两个大的方面谈起。

        1）Canal instance初始化时，根据“消费者的Cursor”来确定binlog的起始位置，但是Cursor在ZK中的保存是滞后的（间歇性刷新），所以Canal instance获得的起始position一定不会大于消费者真实已见的position,这种情况主要出现在主从切换的时候

        2）Consumer端，因为某种原因的rollback，也可能导致一个batch内的所有消息重发，此时可能导致重复消费。

    我们建议，Consumer端需要保持幂等，对于重复数据可以进行校验或者replace。对于非幂等操作，比如累加、计费，需要慎重

# mysql数据库从库同步延迟的问题

在从服务器上执行show slave status;可以查看到很多同步的参数，我们需要特别注意的参数如下,希望文章对各位会有所帮助。

在从服务器上执行show slave status;可以查看到很多同步的参数，我们需要特别注意的参数如下：
Master_Log_File：                      SLAVE中的I/O线程当前正在读取的主服务器二进制日志文件的名称
Read_Master_Log_Pos：        在当前的主服务器二进制日志中，SLAVE中的I/O线程已经读取的位置
Relay_Log_File：                        SQL线程当前正在读取和执行的中继日志文件的名称
Relay_Log_Pos：                        在当前的中继日志中，SQL线程已读取和执行的位置
Relay_Master_Log_File：      由SQL线程执行的包含多数近期事件的主服务器二进制日志文件的名称
Slave_IO_Running：                 I/O线程是否被启动并成功地连接到主服务器上
Slave_SQL_Running：              SQL线程是否被启动
Seconds_Behind_Master：     从属服务器SQL线程和从属服务器I/O线程之间的时间差距，单位以秒计。


