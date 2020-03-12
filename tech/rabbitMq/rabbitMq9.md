
# 从Web端管理RabbitMQ
* RabbitMQ Management插件, 是由Erlang语言编写的，并且和服务器一同运行在同一个Erland VM中。
P177
* 新版服务器发行包已经绑定了该插件，所以无须再进行安装了。唯一要做的就是启用
* ls plugins/
* ./rabbitmq-plugins enable rabbitmq_management
* http://localhsost:55672/mgmt
