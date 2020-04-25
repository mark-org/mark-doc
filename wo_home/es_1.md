
# elasticsearch 分片(Shards)的理解
* ES中所有数据均衡的存储在集群中各个节点的分片中，会影响ES的性能、安全和稳定性
# 分片是什么
* 整个ES集群的核心就是对所有分片的分布、索引、负载、路由等
>> 场景:
假设IndexA有2个分片，我们向IndexA中插入10条数据(10个文档)，那么这10条数据会尽可以平均的分为5条存储在
第一个分片，剩下的5条会存储在另一分片中。
* 和主流关系型数据库的表分区的概念有点类似
# 分片的设置
```
PUT indexName
{
    "settings": {
        "number_of_shards": 5
    }
}

Settings
{
  "settings": {
    "index": {
      "creation_date": "1587518654205",
      "number_of_shards": "1",
      "number_of_replicas": "1",
      "uuid": "Gz90_nmtRxOJNBgLT8E-XQ",
      "version": 

```
* 索引建立后，分片个数是不可以更改的

https://blog.csdn.net/qq_38486203/article/details/80077844



