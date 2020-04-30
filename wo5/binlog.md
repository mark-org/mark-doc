

# 查看是否开启 show variables like '%log_bin%'
log_bin	ON
log_bin_basename	D:\Program Files\MySQL\mysql-8.0.12-winx64\data\binlog
log_bin_index	D:\Program Files\MySQL\mysql-8.0.12-winx64\data\binlog.index
log_bin_trust_function_creators	OFF
log_bin_use_v1_row_events	OFF
sql_log_bin	ON

* 记录表结构变更(create、alter table...)以及表数据修改(insert、update、delete...)的二进制日志
* 不会记录select和show这类操作。（可以通过查询通用日志来查看mysql执行过的所有语句）


# 两类文件
* 索引文件(.index)用于记录哪些日志文件正在被使用
* 日志文件(.00000*)记录数据库所有的DDL和DML(除了数据查询语句)语句事件

* binlog_cache_size:二进制日志缓存部分的大小，默认值32k
* sync_binlog=[N]:表示写缓存多少次，刷一次盘，默认值0

N != 0 mysql用内部XA协议解决一致性问题

# 三个用途
恢复、复制、审计

### 复制
* 主库有一个log dump线程，将binlog传给从库
* 从库有两个线程，一个I/O线程，一个SQL线程，
>> * I/O线程读取主库传过来的binlog内容并写入到relay log. SQL线程从relay log里面读取内容，写入从库的数据库

* 审计：用户可以通过二进制日志中的信息来进行审核，判断是否有数据库进行注入攻击。

# 四个常识 
### format show variables like '%binlog_format%' mysql8默认是row
* statement 记录修改sql语名，准确性差，row(), uuid()等
* row 记录每行实际数据的变更，准确性强，日志文件大
* mixed 上面两者混合，准确性强，大小适中，有可能发生主从不一致问题

业内目前推荐使用的row模式

# 怎样查看
mysqlbinlog
* statement格式：mysqlbinlog mysql-bin.000001
* row格式, -v或者-vv  mysqlbinlog -vv mysql-bin.000001
# mysqlbinlog: unknown variable 'default-character-set=utf8mb4'
mysqlbinlog --no-defaults   mysql-bin.000001


# show binlog events in 'binlog.000131';
show binlog events [IN 'log_name'] [FROM pos] [LIMIT [offset,] row_count];

pos起始点，event_type事件类型 server_id由哪台服务器执行的
end_log_pos post结束点 info执行的sql,

pos和end_log_pos对应二进制文件转换txt后的# at 1196

* 查询第一个(最早的binglog日志)show bindlog events
```
show binlog events in 'mysql-bin.000021' from 8224;
show binlog events in 'mysql-bin.000021' from 8224 limit 10;
show binlog events in 'mysql-bin.000021' from 8224 limit 2,10;
```

# binlog常见参数
log_bin = on off base_nae
sql_log_bin = on off 是否启用
expire_logs_days 日志过期时间 0不过期
log_bin_index 指定binlog.index的路径
binlog_format = mixed row statement
max_binlog_size 文件最大值1073741824=1G
binlog_cache_size
max_binlog_cache_size
sync_binlog= {0 | n} 指定写缓冲多少次，刷一次盘，默认0


# GTID是什么？
GTID 全称A global transaction identifier 全局事物id，是MASTER创建的和事物相匹配的ID号；
为什么要用GTID？
              在主从复制中，尤其是半同步复制中， 由于Master 的dump进程一边要发送binlog给Slave，一边要等待Slave的ACK消息，这个过程是串行的，即前一个事物的ACK没有收到消息，那么后一个事物只能排队候着； 这样将会极大地影响性能；有了GTID后，SLAVE就直接可以通过数据流获得GTID信息，而且可以同步；

             另外，主从故障切换中，如果一台MASTER down，需要提取拥有最新日志的SLAVE做MASTER，这个是很好判断，而有了GTID，就只要以GTID为准即可方便判断；而有了GTID后，SLAVE就不需要一直保存这bin-log 的文件名和Position了；只要启用MASTER_AUTO_POSITION 即可

             当MASTER crash的时候，GTID有助于保证数据一致性，因为每个事物都对应唯一GTID，如果在恢复的时候某事物被重复提交，SLAVE会直接忽略；
show global variables like '%gtid%'




































