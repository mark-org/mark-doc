# redis-cli
* 直接用redis-cli登录
* redis-cli --help
>> * -h -p -s <socket> Server socket(overrides hostname and port)
>> * -a <password>


# 目录结构
* set a:b:c:username simon
* get a:b:c:username

# info
// 
* redis_mode:standalone # 单机或集群
* multiplexing_api:epoll # redis所使用的事件处理模型
* process_id:2568 # 进程ID
* run_id:bad2.... # redis服务器的随机标识符(sentinelt和集群)
* tcp_port:6379
uptime_in_seconds:623 # 启动总时间，秒
uptime_in_days:0	# 天
hz:10 # 内部调度频率：(关闭timeout客户端，删除过期key)
lru_clock:8197344	# 自增时间，用于LRU管理

// # Clients
connected_clients:2
client_longest_output_list:0 # 最长输出列表
client_biggest_input_buf:0 # 最大输入缓存
blocked_clients:0 # 正在等待阻塞命令的客户端数量

// # Memory
user_memory:
user_memory_human:
used_memory_rss: # 从操作系统角度，返回rddis已分配内存总量
used_memory_peak_human: # 内存消耗峰值

used_memory_lua: # lua引擎使用的内存大小

maxmemory:0 

8种内存超过限制之后的响应措施
* redis在占用的内存超过指定的maxmemory之后，通过maxmemory_policy确定redis是否释放内存以及如何释放内存。
>> * noeviction:不做任何的清理工作，在redis的内存超过限制之后，所有的写入操作都会返回错误；但是读操作都能正常的进行;
>> * volatile-lru(least recently used):最近最少使用算法，从设置了过期时间的键中选择空转时间最长的键值对清除掉；
>> ......

### 
Redis五种数据类型：String、Hash、List、Set、SortedSet
Redis中所有的数据都是字符串。命令不区分大小写，key是区分大小写的。Redis是单线程的。Redis中不适合保存内容大的数据。

### SET













