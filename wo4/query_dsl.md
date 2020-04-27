
# Query DSL (Domain Specific Language)
#### Leaf query clauses
* match
```
GET /_search
{
	"query": {
		"match": {
			"message"

"query" : "我的宝马多少马力",
"slop" : 1

```
Short request example

multi_match
```
{
  "query": {
    "multi_match": {
        "query" : "我的宝马多少马力",
        "fields" : ["title", "content"]
    }
  }
}

```
但是multi_match就涉及到匹配评分的问题了
"tie_breaker": 0.3





# es默认采用了lucene的评分公式
用正的浮点数_score来表示相关得分。这个_score 越高，文档的相关性也就越高。
一个查询子句会为每个文档生成一个_score，计算取决于查询子句的类型。
查询子句服务于不同的目的：模糊查询的_score
取决于原始的搜索词与发现的词的拼写的相似度。词的查询会考虑查到的词的比例。一般情况，相关度都是指计算全文的field的内容与全文query串的相


# 关于索引的自动创建禁止与否
dynamic属性有三个值
* true：默认，可以自动创建索引
* false：不自动创建索引,忽略新插入
* strict：精确的，不允许插入不符合默认属性的值，如果不符合，直接报错。

# 关于文档类型的属性
* dynamic_date_formats属性：该属性定义可以识别的日期格式列表；如果文档中有多个字段都是时间格式，可以通用的进行设置。
* dynamic属性：默认为true，

# 关于请求
* GET 请求：获取服务器中的对象
* POST 请求：在服务器上更新对象
* PUT 请求：在服务器上创建对象
* DELETE 请求：删除服务器中的对象HEAD 请求：仅仅用于获取对象的基础信息

# 字段的公共属性：
* index：该属性控制字段是否编入索引被搜索，该属性共有三个有效值：analyzed、no和not_analyzed：store
默认值是no，字段值被分析，能够被搜索，但是，字段值不会存储，这意味着，该字段能够被查询，但是不会存储字段的原始值。
* boost：字段级别的助推，默认值是1，定义了字段在文档中的重要性/权重
* include_in_all：该属性指定当前字段是否包括在_all字段中，默认值是ture，所有的字段都会包含_all字段中；如果index=no，那么属性include_in_all无效，这意味着当前字段无法包含在_all字段中
* copy_to：该属性指定一个字段名称，ElasticSearch引擎将当前字段的值复制到该属性指定的字段中；
* doc_values：文档值是存储在硬盘上的索引时（indexing time）数据结构，对于not_analyzed字段，默认值是true，analyzed string字段不支持文档值;
* fielddata：字段数据是存储在内存中的查询时（querying time）数据结构，只支持analyzed string字段
* null_value：该属性指定一个值，当字段的值为NULL时，该字段使用null_value代替NULL值；在ElasticSearch中，NULL 值不能被索引和搜索，当一个字段设置为NULL值，ElasticSearch引擎认为该字段没有任何值，使用该属性为NULL字段设置一个指定的值，使该字段能够被索引和搜索

# 字符串类型常用的其他属性
* analyzer：该属性定义用于建立索引和搜索的分析器名称
* search_analyzer：该属性定义的分析器，用于处理发送到特定字段的查询字符串；
* ignore_above：该属性指定一个整数值，当字符串字段（analyzed string field）的字节数量大于该数值之后
* position_increment_gap：该属性指定在相同词的位置上增加的gap，默认值是100；
* index_options：索引选项控制添加到倒排索引（Inverted Index）的信息

ES 5.x之后, 为每个text类型的字段新增了名为keyword的子字段, 是不分词的, 默认保留256个字符.
 "query": {
        "term": {
            "name.keyword": "Java编程思想"
        }
    }
* terms query - in检索
```
"terms": {
            "name.keyword": [
                "Java编程思想", "Java并发编程的艺术"
            ]
        }
```
# prefix query - 前缀检索 
—— 扫描所有倒排索引, 性能较差.
"query": {
        "prefix": { "name": "java" }
}

# wildcard query - 通配符检索
扫描所有倒排索引, 性能较差.
"query": {
        "wildcard": { "name": "ja*" }
    }
# regexp query - 正则检索
"query": {
        "regexp": { "name": "jav[a-z]*" }
    }
# boost评分权重 - 控制文档的优先级别
通过boost参数, 令满足某个条件的文档的得分更高, 从而使得其排名更靠前.
"match": { 
{ "match": { "name": "编程思想"} }
...
                        "name": {
                            "query": "艺术", 
                            "boost": 2        // 提升评分权重
                        } 
                    }
# dis_max的提出
如果我们希望检索结果中 (检索串被分词后的) 关键字匹配越多, 这样的文档就越靠前, 而不是多个子检索中匹配少量分词的文档靠前.
⇒ 此时可以使用dis_max和tie_breaker.

# 定制检索结果的排序规则
ES默认是按检索结果的分值(_score)降序排列的.
某些情况下, 可能存在无实际意义的_score, 比如filter时所有_score的值都相同:
"filter": {
                "term": {
                    "author_id": 5520	// 此时所有符合条件的_score都为0
                }
            }

// 或通过constant_score过滤:
