
# http://134.175.231.104:5601/

* D:-> Management / Spaces -> Index Management
* D:-> Management / Spaces -> Index Patterns


* Discover (change)Index

最下面-> Dev Tools 

# del
```
复制代码
//  删除某个document
DELETE /索引名称/type名称/document编号(id)
//  删除整个type
PUT 索引名称/type名称/_delete_by_query?conflicts=proceed
{
  "query": {
    "match_all": {}
  }
}
```

# query
```
GET test-index/_doc/_search
{
  "query": {
    "match_all": {}
  }
}
```











