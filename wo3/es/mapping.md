
# Mapping Field type
### text类型
当一个字段是要被全文搜索的。text类型的字段不用于排序，很少用于聚合(termsAggregation除外)
### keyword
适用于索引结构化的字段，比如email地址、主机名、状态和标签。过滤、排序、聚合。精确值
### date类型
JSON中没有日期类型。
日期格式的字符串：e.g. “2015-01-01” or “2015/01/01 12:10:30”.
long类型的毫秒数( milliseconds-since-the-epoch)
integer的秒数(seconds-since-the-epoch)
### ip类型
用于存储IPV4或者IPV6
### token_count类型
用于统计词频
### geo point类型
地理位置信息类型用于存储地理位置信息的经纬度
### _all
把其它字段拼接在一起的超级字段，所有的字段用空格分开，_all字段会被解析和索引，但是不存储。
### _routing
路由参数
默认的routing值是文件的_id或者_parent，通_routing参数可以设置自定义路由。例如，想把user1发布的
博客存储到同一个分片上，索引时指定routing参数，查询时在指定路由上查询



二、Mapping参数
2.1 analyzer
指定分词器，"analyzer": "ik_max_work", "search_analyzer": "ik_max_work"
2.2 normalizer
用于解析前的标准化配置，比如把所有的字符转化为小写等。例子：在创建的时候，可以自定义多个分词组合等
```
"normalizer": {
	"my_normalizer": {
	  "type": "custom",
	  "char_filter": [],
	  "filter": ["lowercase", "asciifolding"]
	}
}
```
2.3 boost
用于设置字段的权限，比如，关键字出现在title字段的权重是出现在content字段中权重的2倍，设置mapping如下，其中content字段的默认权重是1.


# ES - Index Templates 全局index模板
* 模板匹配规则

# 修改mapping
Elasticsearch的mapping一旦创建，只能增加字段，而不能修改已经mapping的字段。
# 平滑过渡(访问同义词)
采取什么合理设计呢？就是我们的程序访问索引库时，始终使用同义词来访问，而不要使用真正的indexName。
在reindex完数据之后，修改之前的同义词即可
# 过程
1. 创建一个索引，最好带上版本号_v1
2. 创建一个同义词
```
curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "add": {
            "alias": "my_index",
            "index": "my_index_v1"
        }}
    ]
}
'

curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "remove": {
            "alias": "my_index",
            "index": "my_index_v1"
        }},
        { "add": {
            "alias": "my_index",
            "index": "my_index_v2"
        }}
    ]
}
'
curl -XDELETE localhost:9200/my_index_v1


```
# elasticsearch 索引复制 数据
```
http://localhost:9200/_reindex
{

  "source": {
    "index": "old_index"
  },
  "dest": {
    "index": "new_index",
    "op_type": "create"
  }
}
``` 

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

































