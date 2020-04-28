
# highlight
"query": {
	"match_phrase": ...
},
"highlight": {
	"fields": {
		"about': {}
	}
}
# aggregations
{
	"aggs": {
		"all_interests': {
			"items": {"field": "interests"}
		}
	}
}


# 空集群
如果我们启动一个单独的节点，它还没有数据和索引 CLUSTER: NODE1-*MASTER
一个node就是一个Elasticsearch实例，而一个集群cluster由一个或多个节点组成.
它们具有相同的cluster.name,它们协同工作，分享数据和负载。当加入新的节点或者删除一个节点时，
集群就会感知到并平衡数据。

集群中一个节点会被选举为主节点master,它将临时管理集群级别的一些变更，例如新建或删除索引、
增加或移除节点等。主节点不参与文档级别的变更或搜索，这意味着在流量增长的时候，该主节点不会成为
集群的瓶颈。任何节点都可以成为主节点。

做为用户，我们能够与集群中的任何节点通信，包括主节点。每一个节点都知道文档存在于哪个节点上，它们
可以转发请求到相应的节点上。 我们访问的节点负责收集各节点返回的数据，最后一起返回给客户端。

# 集群健康
GET/_cluster/health 集群健康有三种状态:green、yellow或red
green 所有主要分片和复制分片都可用
yellow 所有主要分片可用，但不是所有复制分片都可用
red 不是所有的主要分片都可用
### primary shard 和 replica shard















