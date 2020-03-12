
https://www.rabbitmq.com/tutorials/amqp-concepts.html

https://www.jianshu.com/p/24e541170ace

# AMQP 0-9-1 Model Explained
(Advanced Message Queuing Protocol) is a messaging protocal that enables conforming client
applications to communicate with conforming messaging middleware brokers.

# Message Broker(代理服务器)
* 接收和分发消息的应用，RabbitMQ Server就是消息代理服务器，其中包含概念很多：
* 信道channel 队列queue 交换器exchange 路由键routin key 绑定binding key 虚拟主机vhost等
* Since it is a network protocol, the publishers, consumers and the broker can call reside on different machines.

### MQ生产分组消息、消息分组消息需求
* 队列消息需要多个线程消费者去消费，但是每个消费者，虽然mq支持多个消费者，但是，每个消费者消费的数量可能不同，有的线程跑到快，
  就肯定消费多一些
* 现在的需求是每个线程消费的数量一样，这就需要用到mq分组了

### Exchanges and Exchage Types
* Exchange type 	Defalut pre-declared names
  Direct exchange   (Empty string) and amq.direct
  Fanout exchange	amq.fanout
  Topic exchange	amq.topic
  Headers exchange	amq.match(and amq.headers in RabbitMQ)
  
### Exchanges are declared with a number of attributes. the most important of which are:
* Name
* Durability (exchanges survice broker restart)
* Auto-delete (exchanges is deleted when last queue is unbound from it)
* Arguments (optional, used by plugins and broker-specific features)

### Topic Exchange
* Topic Exchange交换机也叫通配符交换机，Topic Exchange主要有两种通配符：# 和 * 
* *（星号）：可以（只能）匹配一个单词
* #（井号）：可以匹配多个单词（或者零个）
* 当binding key不包含”*”和”#”时，这类似于我们上一章说的Direct Exchange直连交换机模式。
* 当一个队列被绑定为binding key为”#”时，它将会接收所有的消息，这类似于广播形式的交换机模式。

### Queues
* Queues in the AMQP 0-9-1 model are very similar to queues in other message- and task-queueing system:
** Name
** Durable (the queue will survice a broker restart)
** Exclusive (used by only one connection and the queue will be deleted when that connection closes)
** Auto-delete (queue that has had at least one consumer is deleted when last consumer unsubscribes)
**Arguments(optional; used by plugins and broker-specific features such as message TTL, queue length limit, etc)


# Message Acknowledgements
* Since networks are unreliable and applications fail, it is often necessay to have some kind of processiing acknnowldegement.
* The operations above form logical pairs: exchange.declare and exchange.decalre-ok exchange.delete and exchang.delete-ok

### Connections
AMQP 0-9-1 connections are typically long-lived. 
### Channels
Some applications need multiple connections to the broker.Hoverver, it is undesirable to key many TCP connections open
at the some time because doing so consumes system resources and makes it more difficult to configure firewarll.AMQP 0-9-1
connections are multiplexed with channels that can be thought of as "lightweight connections that share a single TCP connection"

For applications that use multiple threads/processes for processing, it is very commono to open a new channel per thread/process 
and not share channels between them.











