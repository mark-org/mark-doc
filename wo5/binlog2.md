
# show binary logs
二进制日志文件默认会存放在 /var/lib/mysql 目录下
windows MySQL\mysql-8.0.12-winx64\data

# $ mysqlbinlog -v mysqld-bin.000001
# 指定数据库名称 -d(--database)
使用 -d 选项，可以指定一个数据库名称
mysqlbinlog -d crm mysqld-bin.000001 > crm-events.tx
# Binlog日志的生成规则
* 通常情况下，当前binlog大小超过500MB或超过6小时会切换到下一序号文件继续写入，即写满500MB或超过6小时就会生成新的binlog日志文件。新的binlog文件继续写入，老的binlog文件并不会立刻上传，会异步上传。
* 有些情况下，binlog日志不满500MB就不再写入，比如由于命令的执行、系统重启等原因。
* 有些情况下，会出现binlog文件尺寸超过500MB的情况，比如当时在执行大事务，不断写入binlog导致当前binlog文件尺寸超过500MB。

# 禁恢复过程产生日志(-D --disable-log-bin)
mysqlbinlog -D mysql-bin.000001 /*!32316 SET @OLD_SQL_LOG_BIN=@@SQL_LOG_BIN, SQL_LOG_BIN=0*/;

# 在输出中控制base-64 BINLOG 

--base64-output
$ mysqlbinlog --base64-output=never mysqld-bin.000001
never: 
?????

# 跳过前N个条件
-o 偏移
mysqlbinlog -o 10 mysqld-bin.000001

# 从一个特定位置提取条目
mysqlbinlog -j 15028 mysqld-bin.000001 > from-15028.out

# 将条目截止到一个特定的位置
$ mysqlbinlog --stop-position=15028 mysqld-bin.000001 > upto-15028.output

# 在输出中只显示语句
如果只想查看常规的SQL语句，而不需要其他内容，那么可以使用 -s (--short-form) 选项

# 查看特定开始时间的条目 *******************************
$ mysqlbinlog --start-datetime="2020-04-30 12:42:42" mysqld-bin.000001

# 查看特定结束时间的条目 ********************************
$ mysqlbinlog --stop-datetime="2017-08-16 15:00:00" mysqld-bin.000001

# 从远程服务器获取二进制日志 (-R选项与-read-from-remote-server)
$ mysqlbinlog -R -h 192.168.101.2 -p mysqld-bin.000001





### 恢复数据
执行命令：/usr/bin/mysqlbinlog --start-datetime="2018-04-27 20:57:55" --stop-datetime="2018-04-27 20:58:18" --database=hello /var/lib/mysql/mysql-bin.000009 | /usr/bin/mysql -uroot -p8856769abcd -v hello  更改的数据得到了恢复
执行命令/usr/bin/mysqlbinlog --start-datetime="2018-04-27 20:58:18" --stop-datetime="2018-04-27 20:58:35" --database=hello /var/lib/mysql/mysql-bin.000009 | /usr/bin/mysql -uroot -p8856769abcd -v hello  插入的数据得到了恢

























