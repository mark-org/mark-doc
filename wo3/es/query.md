
# query
```
GET /_search
{
    "query": YOUR_QUERY_HERE
}

#（empty search） —{}— 在功能上等价于使用 match_all 查询

{
    QUERY_NAME: {
        ARGUMENT: VALUE,
        ARGUMENT: VALUE,...
    }
}
# 针对某个字段
{
    QUERY_NAME: {
        FIELD_NAME: {
            ARGUMENT: VALUE,
            ARGUMENT: VALUE,...
        }
    }
}

{
    "match": {
        "tweet": "elasticsearch"
    }
}
# 完整的
GET /_search
{
    "query": {
        "match": {
            "tweet": "elasticsearch"
        }
    }
}

# 合并查询语句 一个 bool 语句 允许在你需要的时候组合其它语句
{
    "bool": {
        "must":     { "match": { "tweet": "elasticsearch" }},
        "must_not": { "match": { "name":  "mary" }},
        "should":   { "match": { "tweet": "full text" }},
        "filter":   { "range": { "age" : { "gt" : 30 }} }
    }
}

```

# https://www.elastic.co/guide/cn/elasticsearch/guide/current/_queries_and_filters.html






















