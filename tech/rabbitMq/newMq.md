
# Connections -> Channel
* Channel:192.168.101.232.27819(1) User name redsea
>> * Mode? C-confirm Channel will send streaming publish confirmations.
>> * T-transactional Channel is transactional

### 生产者确认模式实现原理
* 生产者将信道设置成confirm模式，一旦信道进入confrim模式，所有在该信道上面发布的消息都将会被指派一个唯一的ID(从1开始),
  一旦消息被投递到所有匹配的队列之后，broker就会发送一个确认给生产者(包含消息的唯一ID)，这就使得生产者知识消息已经正确
  到达目的的队列了，如果消息和队列是可持久化的，那么好确认消息会将消息写入磁盘之后发出，broker回传给生产者的确认消息中
  delivery-tag域包含了确认消息的序列号，此外broker也可以设置basic.ack的multiple域，表示到这个序列号之前的所有消息都已经
  得到处理。
  
### broker
* broker是指一个或多个erlang node的逻辑分组，且node上运行着RabbitMq应用程序。
* cluster是在broker的基础上，增加了node之间共享元数据的约束。

* broker:消息队列服务器实体

### Consumers
* Consumer Tags:Every consumer has an identifier that is used by client libraries to invoke for a given delievery.
amq.ctag-b1xQZccD8f-th-FpaHFbWg   Their names vary from protocal to protocol. Consumer tags and subscription IDs 
are two most commonly used terms. RabbitMQ documentation tends to use the fromer.
* Consumer Lifecycle

### Connection Recovery
* Client can lose their connection to RabbitMQ. When connection loss is detedted.message delivery stop.
* Some client libraries offer automatic connection recovery features that involves consumer recovery.

### Consumers active
* Whether the consumer is active or not, i.e whether the consumer can get messages from the queue.
  When single active consumer is enabled for the queue, only one consumer at a time is active.
  When single active consumer is disabled for the queue, consumer are active by default. 


### RabbitMQ消费者的几个参数
* prefetchCount(prfetch) : The number of messages to accept from the broker in one socket frame.
  The higher this is the faster the messages can be delivered, but the higher the risk of non-sequential processing.
  Ignored if the acknowledgeMode is NONE. This will be increased, if nessary, to match the txSize.

* concurrentConsumers(concurrency)
  The number of concurrent consumers to initially start for each listener。

* concurrency设置的是对每个listener在初始化的时候设置的并发消费者的个数。
* prefetch是每次从一次性从broker里面取的待消费的消息的个数

图中可以看出有两个消费者同时监听Queue，但是注意这里的消息只有被一个消费者消费掉就会自动ack
，另外一个消费者就不会再获取到此消息，Prefetch Count为配置设置的值3，意味着每个消费者每次会预取3个消息准备消费。
每个消费者对应的listener有个Exclusive参数，默认为false,
 如果设置为true，concurrency就必须设置为1，即只能单个消费者消费队列里的消息，适用于必须严格执行消息队列的消费顺序（先进先出）。




### ACK机制 （重复处理？）
* 每个Consumer可能需要一段时间才能处理完收到的数据。如果在这个过程中，Consumer出错，异常退出了，而数据还没有处理完成，
  那么非常不幸，这段数据就丢失了。因为我们采用no-ack的方式进行确认，也就是说，每次Consumer撞到数据后，而不管是否处理完成，
  RabbitMQ Server会立即把这个Message标记为完蛋，然后从queue中删除了。
* 这里并没有用到超时机制。RabbitMQ仅仅通过Consumer的连接中断来确认该Message并没有被正确处理。也就是说，rabbitMq给了
  Consumer足够长的时间来做数据处理。

如果忘记了ack，那么后果很严重。当Consumer退出时，Message会重新分发。然后RabbitMQ会占用越来越多的内存，
由于 RabbitMQ会长时间运行，因此这个“内存泄漏”是致命的。去调试这种错误，可以通过一下命令打印un-acked Messages.

* 如果连接没有断开应用要通知服务器让消息重新发送：
可以通过channel.nack(message)来让不通过的消息再次进入消息队列。
if(body==’Hello World3!’){chnl.nack(msg); //这样就可以让这个消息再次进入队列而不用重启服务。
}else{console.log(‘ack’);chnl.ack(msg);}



### 自动ack会导致消息丢失的问题：
把自动应答true改false,并在消息处理完后发ack响应。
* 注：自动ack还有个弊端，只要队列不空，rabbitMQ会源源不断的把消息推送给客户端，而不管客户端能否消费的完

### 启用ack机制后，没有及时ack导致的队列异常：
* callback触发了一个bug，导致所有消息都抛出异常，然后队列的Unacked消息数暴涨，导致MQ响应越来越慢，甚至崩溃的问题
* 原因是如果MQ没得到ack响应，这些消息会堆积在Unacked消息里，不会抛弃，直到客户端断开重连时，才变回ready;
如果Consumer客户端不断开连接，这些Unacked消息，永远不会变回ready状态，Unacked消息多了，占用内存越来越大，就会异常了。
解决办法就是及时去act消息了

### 启用nack机制后，导致的死循环

### 启用Qos和ack机制后，没有及时ack导致的队列堵塞

### 消费者串行处理，崩溃时导致未处理的预取数据丢失

### 心跳时间设置太短导致的异常


# RabbitMQ的ack或nack机制使用不当导致的队列堵塞或死循环问题
https://blog.csdn.net/youbl/article/details/80425959?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task


  




