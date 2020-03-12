
# INFORMATION_SCHEMA下的INNODB_LOCKS和INNODB_LOCK_WAITS表已被删除。
 用performance_schema data_locks和data_lock_waits表替代

```sql
select * from information_schema.tables

select * from performance_schema.data_locks -- 查看正在锁的事物

select * from performance_schema.data_lock_waits -- 查看正在锁的事物


show full processlist;



show engine innodb status;
show status like '%lock%';
```


*  MySQL默认不能实时查看执行的SQL语句，因为这会消耗一定的资源。
SHOW VARIABLES LIKE "general_log%";
SET GLOBAL general_log = 'ON';
2.2 永久开启
永久有效需要配置my.cnf文件，加入下面两行：

general_log = 1
general_log_file = /var/log/mysql/general_sql.log

# 正在运行的sql
```
SELECT st.* FROM performance_schema.events_statements_current st
```









