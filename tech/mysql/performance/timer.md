
https://dev.mysql.com/doc/refman/8.0/en/performance-schema-timing.html

# Performance Schema Timers
```
SELECT * FROM performance_schema.performance_timers;

```

# 正在执行的SQL
```
show processlist

-- 8
select * from performance_schema.threads where processlist_info is not null
-- 8之前
select * from information_schema.`PROCESSLIST` where info is not null;

```




