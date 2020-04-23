
# es
http://134.175.231.104:9200/

# kibana
http://134.175.231.104:5601/

# Query DSL
Elasticsearch provides a full Query DSL(Domain Specific Language) based on JSON to define queires.

# python api
https://elasticsearch-py.readthedocs.io/en/master/

# Kibana
1.点击左边的D
Elasticsearch -> Index Management


# health
curl -XGET http://134.175.231.104:9200/_cluster/health?pretty=true
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 5,
  "active_shards" : 5,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 1,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 83.33333333333334
}

# 处理Elasticsearch集群yellow和red状态
* red表示不是所有的主分片都可用，通常时由于某个索引的住分片为分片unassigned，只要找出这个索引的分片，手工分配即可
* yellow表示所有主分片可用，但不是所有副本分片都可用，最常见的情景是单节点时，由于es默认是有1个副本，主分片和副本不能在同一个节点上，所以副本就是未分配unassigned

* 处理
>> * 过滤查看所有未分配索引的方式curl -s "http://134.175.231.104:9200/_cat/shards" | grep UNASSIGNED
第一列表示索引名，第二列表示分片编号，第三列p是主分片，r是副本

* 分配分片
知道哪个索引的哪个分片就开始手动修复，通过reroute的allocate分配
```
curl -XPOST '{ESIP}:9200/_cluster/reroute' -d '{
    "commands" : [ {
          "allocate" : {
              "index" : "eslog1",
              "shard" : 4,
              "node" : "es1",
              "allow_primary" : true
          }
        }
    ]
}'
```
# 创建索引时，需要创建多少个分片？
* 在生产环境中, 随着数据集的增长, 不合理的分配策略可能会给系统的扩展带来严重的问题.

* 集群(cluster):由一个或多个节点组成, 并通过集群名称与其他集群进行区分
* 节点(node):单个ElasticSearch实例. 通常一个节点运行在一个隔离的容器或虚拟机中
* 索引(index):在ES中, 索引是一组文档的集合
* 分片(shard):因为ES是个分布式的搜索引擎, 所以索引通常都会分解成不同部分, 而这些分布在不同节点的数据就是分片. 
ES自动管理和组织分片, 并在必要的时候对分片数据进行再平衡分配, 所以用户基本上不用担心分片的处理细节，一个分片默认最大文档数量是20亿.
* 副本(replica):ES默认为一个索引创建5个主分片, 并分别为其创建一个副本分片. 也就是说每个索引都由5个主分片成本, 而每个主分片都相应的有一个copy.

### 分片(shard)
* 索引通常都会分解成不同部分，而这些分布在不同节点的数据就是分片
* 一个分片默认最大文档数量是20亿
### 副本(replica)
* 主分片的一个copy


对于分布式搜索引擎来说, 分片及副本的分配将是高可用及快速搜索响应的设计核心.
主分片与副本都能处理查询请求, 它们的唯一区别在于只有主分片才能处理索引请求.

* 请记住, 索引的number_of_shards参数只对当前索引有效而不是对整个集群生效.
对每个索引来讲, 该参数定义了当前索引的主分片数(而不是集群中所有的主分片数).


* 副本对搜索性能非常重要, 同时用户也可在任何时候添加或删除副本. 正如另篇文章所述, 
额外的副本能给你带来更大的容量, 更高的呑吐能力及更强的故障恢复能力.

* 主分片的配置与硬盘分区很类似, 在对一块空的硬盘空间进行分区时, 会要求用户先进行数据备份, 然后配置新的分区, 最后把数据写到新的分区上.



###  你分配的每个分片都是有额外的成本的:
* 每个分片本质上就是一个Lucene索引, 因此会消耗相应的文件句柄, 内存和CPU资源
* 每个搜索请求会调度到索引的每个分片中. 如果分片分散在不同的节点倒是问题不太. 但当分片开始竞争相同的硬件资源时, 性能便会逐步下降
* ES使用词频统计来计算相关性. 当然这些统计也会分配到各个分片上. 如果在大量分片上只维护了很少的数据, 则将导致最终的文档相关性较差

# ElasticSearch推荐的最大JVM堆空间是30~32G, 
所以把你的分片最大容量限制为30GB, 然后再对分片数量做合理估算. 例如, 你认为你的数据能达到200GB, 我们推荐你最多分配7到8个分片.

# Elasticsearch中的数据组织成索引
每一个索引由一个或多个分片组成。每个分片是Luncene索引的一个实例，你可以把实例理解成自管理的搜索引擎，用于在Elasticsearch集群中对一部分数据进行索引和处理查询。




### ES mapping
* 映射是定义一个文档以及其所包含的字段如何被存储和索引的方法
如：
* 哪些string类型的field应当被当成full-text字段
* 哪些字段应该是数值类型、日期类型或者是地理位置信息
* 日期类型字段的格式是怎么样的
* 是否文件的所有字段都需要被索引到_all字段
* 动态增加的field可以由用户自定义的模板来控制其行为

### 映射类型(mapping types)
每一个映射类型都包含以下内容:
1. 元数据字段
定义如何处理关联文档的元数据。_index, _type, _id, _source
2. 字段列表和属性
### 字段数据类型(field datatypes)
1. 基本数据类型 string, long, boolean, ip
2. JSON分层数据类型 object, nested
3. 特殊类型 geo_point, geo_shape, completion
### 动态映射(dynamic mappging)

* updating existing mappings
* fields are shared across mapping types

## field datatypes
* 基本类型
1. 字符串(full-text和keywords)
full-text会被分析，keywords只能作为一个精确值查询
2. 数值
long, integer, short, byte, double, float
3. 日期，JSON本身并没有日期数据类型，在ES中的日期类型可以是：
* "20165-01-01" or "2015/01/01 12:10:30"的字符串
* long类型毫秒级
* int类型的秒级别
日期类型默认会被转换为UTC并且转换为毫秒级别的时间戳的long类型存储
4. 布尔
假：false "false" "off" "no" "0" "", 0, 0.0
真：不假
5. 二进制
* 二进制类型以Base64编码方式接收一个二进制值，二进制类型字段默认不存储，也不可搜索。

### 复杂类型
JSON格式本身是分层级的--文档可以包含对象，对象还可以包含子对象。不过，在ES内部"对象"被索引为一个扁平的键值对。
转换为: "manager.name.last": "Smith"

### 数组
["one", "two"] [1, 2]


# Meta-Fields
文档标识相关元数据字段
_index
* 当执行多索引查询时，可能需要添加特定的一些与文档有关的索引的子句。
* _index字段可以用在term、terms查询，聚合(aggregations)操作，脚本(script)操作以及用来排序(sort).
_type
* 可以用来让针对具体type的搜索更加快
* 可以用在querys、aggregations、scripts以及sorting
_source
* 存放的是文档的原始JSON信息
* 不被indexed，不过被stored，所以可以通过get或search取得该字段的值.

# 索引操作相关元数据字段
_all
* _all字段把其他所有字段的内容存储到一个大的字符串，不管其它字段是什么数据类型，在_all中都被当作字符串处理
* 每个index只有一个_all字段
* 该字符串会被analyzed和indexed，但不会store。可以被搜索，但无法用来恢复。
* _all字段也和普通字符串字段一样可以接收：analyzer、term_vectors、index_options和store等参数
* 生成_all字段是有资源消耗的，会消耗CPU和disk存储



# query_string和simple_query_string，默认就是查询_all字段

query_string,simple_query_string与match查询的区别在于前者的查询,语法是写在query里面的,后者是通过json的数据结构来查询另外前者对于多字段的查询比较好
另外前者对于多字段的查询比较好
query_string和simple_query_string的区别在于对'and or not'等查询的支持上,比如在query_string的情况下'Pantheon AND LEO',这句话如果解析是查询必须要同时包含PATHEON和LEO,而simple_query_string则是将其分词成Pantheon,AND和LEO,默认的operator为OR




# /_analyze
Content-Type application/json;charset:utf-8
http://134.175.231.104:9200 /test-index/_analyze
{"analyzer" : "standard",  "text" : "Elasticsearch"}

_analyze是Elasticsearch一个非常有用的API，它可以帮助你分析每一个field或者某个analyzer/tokenizer是如何分析和索引一段文字。


token是一个实际被存储在索引中的词
position指明词在原文本中是第几个出现的
start_offset和end_offset表示词在原文本中占据的位置。


也可以用指定的analyzer来分析使用whitspace
{"analyzer":"whitespace", "text":"床前 明月光"}

使用ik分析器  "analyzer": "ik_max_word",

安装ik
https://github.com/medcl/elasticsearch-analysis-ik/releases/tag/v7.5.1
将文件复制到 es的安装目录/plugin/ik下面即可

ik_max_word：会将文本做最细粒度的拆分，比如会将“中华人民共和国国歌”拆分为“中华人民共和国,中华人民,中华,华人,人民共和国,人民,人,民,共和国,共和,和,国国,国歌”，会穷尽各种可能的组合；
ik_smart：会做最粗粒度的拆分，比如会将“中华人民共和国国歌”拆分为“中华人民共和国,国歌”


PUT /school_index
{
    "settings" : {
        "index" : {
            "analysis.analyzer.default.type": "ik_max_word"
        }
    }
}




























































