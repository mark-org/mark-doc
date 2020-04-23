

# ES
cd /home/search/action/elasticsearch-7.5.1/bin
su search
/home/search/action/elasticsearch-7.5.1/logs/elasticsear                                                               ch.log (Permission denied)

# 日志权限和属主导致启动失败chmod chown

nohup ./elasticsearch &

http://134.175.231.104:9200/

# kibana
http://134.175.231.104:5601
ps aux|grep node
lsof -i:端口号



# 简介
ELK软件栈
Logstash负责数据的采集，处理（丰富数据，数据转型等）
Kibana负责数据展，分析及管理
Elasticsearch处于最核心的位置，它可以帮我们对数据进行快速地搜索及分析


# ES
https://blog.csdn.net/UbuntuTouch/article/details/98871531








