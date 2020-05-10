

# canal [kə'næl]
当前的 canal 支持源端 MySQL 版本包括 5.1.x , 5.5.x , 5.6.x , 5.7.x , 8.0.x

# MySQL主备复制原理
* MySQL master将数据变更写入二进制日志(binary log)
其中记录叫做二进制日志事件binary log events，可以通过show binlog events进行查看
* MySql slave将master的binary log events拷贝到它的中继日志(relay log)
* MySql slave重放relay log中事件，将数据变更反映它自己的数据

# canal工作原理
* cannal模拟MySQL slave的交互协议，伪装自己为MySQL slave,向MySQL master发送dump协议
* Mysql master收到dump请求，开始推送binary log给slave(即canal)
* canal解析binary log对象(原始为byte流)

# 客户端
canal java 客户端: https://github.com/alibaba/canal/wiki/ClientExample
canal 消费端开源项目: Otter 客户端项目 https://github.com/alibaba/otter

# QuickStart
[mysqld]
log-bin=mysql-bin # 开启 binlog
binlog-format=ROW # 选择 ROW 模式
server_id=1 # 配置 MySQL replaction 需要定义，不要和 canal 的 slaveId 重复

* 授权canal链接mysql 
```
CREATE USER canal IDENTIFIED BY 'canal';  
GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal'@'%';
-- GRANT ALL PRIVILEGES ON *.* TO 'canal'@'%' ;
FLUSH PRIVILEGES;
```

 https://github.com/alibaba/canal/wiki/QuickStart
 
 # canal.instance.tsdb.enable
 v1.0.25版本新增,是否开启table meta的时间序列版本记录功能

# https://github.com/alibaba/canal/wiki/ClientExample


# canal正则配置读取多个库表
canal/conf/example/instance.properties
文件中配置正则匹配多个库表。

canal.instance.filter.regex =155_155\\..*,cms\\.measurementvalues
canal.mq.partition=0
canal.mq.topic= SKF
canal.mq.partitionHash=155_155\\..*:id,cms\\.measurementvalues:MeasurementValueID
canal1.13之后可以使用 , （逗号）隔离匹配规则
上面含义为匹配
155_155库下所有表（\需要转义所以需要两个）
cms库下的measurementvalues表

第一个根据id取hash 第二个正则根据MeasurementValueID取hash

# table regex 设置白名单，如果在instance.properties配置文件中进行该项配置，则在代码中不应该再配置
# connector.subscribe(".*\\..*");，如果还在代码中配置，则配置文件将会失效！！！
canal.instance.filter.regex = .*\\..*
# table black regex 设置黑名单
canal.instance.filter.black.regex =

所以当你只关心部分库表更新时，设置了canal.instance.filter.regex，一定不要在客户端调用CanalConnector.subscribe(".*\\..*")，
不然等于没设置canal.instance.filter.regex。
如果一定要调用CanalConnector.subscribe(".*\\..*")，
那么可以设置instance.properties的canal.instance.filter.black.regex参数添加黑名单，过滤非关注库表。


mysql 数据解析关注的表，Perl正则表达式.多个正则之间以逗号(,)分隔，转义符需要双斜杠(\\) 
常见例子：
1. 所有表：.* or .*\\..*
2. canal schema下所有表： canal\\..*
3. canal下的以canal打头的表：canal\\.canal.*
4. canal schema下的一张表：canal.test1
5. 多个规则组合使用：canal\\..*,mysql.test1,mysql.test2 (逗号分隔)
注意：此过滤条件只针对row模式的数据有效(ps. mixed/statement因为不解析sql，所以无法准确提取tableName进行过滤)



















