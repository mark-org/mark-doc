
# ES
向Elasticsearch发出的请求的组成部分与其它普通的HTTP请求是一样的：
```
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'

# -X参数指定 HTTP 请求的方法。
# -d参数用于发送 POST 请求的数据体。
# 使用-d参数以后，HTTP 请求会自动加上标头Content-Type : application/x-www-form-urlencoded。并且会自动将请求转为 POST 方法，因此可以省略-X POST。
# -i返回HTTP头curl -i -XGET 'localhost:9200/'
```
VERB: GET , POST , PUT , HEAD , DELETE
PORT默认9200 
PATH _count将返回群集中文档的数量(_nodes/stats/jvm?pretty, 
BODY json格式

```
curl -XGET 'http://134.175.231.104:9200/_count?pretty' -d '
{
	"query": {
		"match_all": {}
	}
}
'
```
P23
```
curl -s -H "Content-Type: application/json" -XPUT http://134.175.231.104:9200/test-index/_doc/1000 -d '{"author": "deng"}'
```



