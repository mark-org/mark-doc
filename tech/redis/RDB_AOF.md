# RDB(默认)和AOF
* rdb(Redis DataBase)功能核心函数rdSave(生成rdb文件)和rdbLoad(从文件加载内存)两个函数
* AOF(Append-only file)

### RDB
* 在指定的时间间隔内，执行指定次数的写操作，则会将内存中的数据写入到磁盘中。
即在指定目录下生成一个dump.rdb文件。Redis 重启会通过加载dump.rdb文件恢复数据。
```
save <seconds> <changes> # save <指定时间间隔> <执行指定次数更新操作>
# 默认是 900秒内有1个更改，300秒内有10个更改以及60秒内有10000个更改，则将内存中的数据快照写入磁盘。
save "" # 取消
dbfilename dump.rdb
dir ./
rdbcompression yes # 默认开启数据压缩
```

### RDB 的优缺点
* 优点
>> * 1 适合大规模的数据恢复。
>> * 2 如果业务对数据完整性和一致性要求不高，RDB是很好的选择。
* 缺点
1 数据的完整性和一致性不高，因为RDB可能在最后一次备份时宕机了
2 备份时占用内存，因为Redis 在备份时会独立创建一个子进程，将数据写入到一个临时文件（此时内存中的数据是原来的两倍哦），最后再将临时文件替换之前的备份文件。
* 所以Redis 的持久化和数据的恢复要选择在夜深人静的时候执行是比较合理的。

### AOF
* AOF ：Redis 默认不开启。它的出现是为了弥补RDB的不足（数据的不一致性），所以它采用日志的形式来记录每个写操作，并追加到文件中。
Redis 重启的会根据日志文件的内容将写指令从前到后执行一次以完成数据的恢复工作。
* 1 redis 默认关闭，开启需要手动把no改为yes
```
appendonly yes
appendfilename "appendonly.aof"

# 指定更新日志条件
# appendfsync always （慢，安全）
appendfsync everysec
# appendfsync no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

