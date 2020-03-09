# hello world生产者
1. 建立到代理服务器的连接 connection (默认虚拟主机"/", 默认端口5672, guest/guest)
2. 获得信道 channel
3. 声明交换器 exchange="hello-exchange", type="direct", passive=False,durable=True, auto_delete=False
4. 创建纯文件消息 content_type = "text/plain"
5. 发布消息 body=msg, exchange="hello-exchange", properties=msg_props, routing_key="hola"

# 参数
* auto_delete=True没有消息者时自动删除，适用于临时队列
* passive=True，如果用户想查义某一个队列是否已存在，如果不存在，不想建立该队列，仍然可以调用queue.delcare,
  只不过需要将参数passive设为true，传给queue.delcare，如果该队列已存在，则会返回true；如果不存在，则会返回Error,
  但是不会创建新的队列

# hello world消费者
1. 建立到代理服务器的连接
2. 获得信道
3. 声明交换器
4. 声明队列 channel.queue_declare(queue="hello-queue" 
5. 通过键"hola"将队列和交换器绑定起来 channel.queue_bind(......routing_key="hola")
6. 用于处理传入的消息的函数 msg_consumer
7. 消息确认 channel.basic_ack(delivery_tag=method.delivery_tag)
8. 停止消费并退出
9. 订阅消费者 channel.basic_consume(msg_consumer, queue="hello-queue", cconsumer_tag="hello-consumer"
10. 开始消费 channel.start_consuming()

# 带有确认功能的hello world生产者
1. def confirm_handler(frame): 发送方确认模式处理器
2. channel.confirm_delivery(callback=confirm_handler) 将信道设置为confirm模式
3. msg_ids = [] 重设消息ID追踪器
4. channel.basic_publicsh 发布信息
5. msg_ids.append(len(msg_ids) + 1) 将ID添加到追踪列表中

# Erlang也有虚拟机
* 而虚拟机的每个实例我们称之为节点(node).
* 不同于JVM，多个Erlang应用程序可以运行在同一个节点为之上.
* 节点之间可以进行本地通信(不管它们是不是真的在同一台服务器上)

* 启动：./sbin/rabbitmq-server 日志:/var/log/rabbitmq/目录下找到名为rabbti@[hostname].log的日志文件
  -detached守护程序的方式在后台运行
* 停止：./sbin/rabbitmqctl stop(会和本地节点通信并指示其干净地关闭)
* 停止远程节点: -n rabbit@[hostname]

# 有时你只想要重启RabbitMQ应用程序，而同时保持通Erlang节点运行。
* 对集群来说，这种做法是必要的。为了把节点加入现有的集群当中，你需要做的是停止应用程序，把节点重置为原始状态。
  这样节点就准备好加入集群了。./rabbitmqctl stop_app


# Rabbit配置文件
* /etc/rabbitmq/rabbitmq.config(文件位置可以通过rabbitmq-server脚本对CONFIG_FILE环境变量进行设置)
```
[{mnesia, [{dump_log_write_threadshold, 1000},{}]
```
是一个包含了嵌套哈希表(字典或者命令数组)的数组。
* rabbitmq中的每个队列、交换器和绑定的元数据(除了消息的内容)都是保存到Mnesia的。
* Mnesia是内建在Erlang的非SQL型数据库。
* Mnesia的dump_log_write_threshold选项控制着转储的频度。将其设置成1000就告诉Mensia,
  每1000个条目就转储日志内容到数据库文件。
* tcp_listeners [{"0.0.0.0", 5672}] 非ssl
* ssl_listeners ssl_options 证书

* vm_memory_high_watermark 0.4 允许使用的安装内存百分比0.4 = 40%
* msg_store_file_limit(字节) 16,777,216  		RabbitMQ垃圾收集存储内容之前，消息存储数据库的最大大小
* queue_index_max_journal_entries	262144 		在转储到消息存储数据库并提交之前，消息存储日志里最大条目数

# Rabbit权限
RabbitMQ权限工作原理：用户可以为连接到RabbitMQ主机的应用程序设置不同级别的权限(读、写、和/或配置)
```
# 创建用户和删除用户 查看用户
./rabbitmqctl add_user cashing-tier cashMel
./rabbitmqctl delete_user cashing-tier 
./rabbitmqctl list_users
./rabbitmqctl change_password cashing-tier comxxxx
```
* 你想要授予cashing-tier(vhost=sycamore)完全的访问权限(配置、写和读权限)
```
./rabbitmqctl set_permissions -p sycamore \
cashing-tier ".*" ".*" ".*"

```

# 列出队列和消息数目
```
./rabbitmqctl list_queues
./rabbitmqctl list_queues -p sycamore
./rabbtimqctl list_queues name durable auto_delete
./rabbtimqctl list_queues name messages consumers memory
```

# 查看交换器和绑定
.....

# 查看数据统计
-p 虚拟主机或者路径信息, 默认是"/"



















