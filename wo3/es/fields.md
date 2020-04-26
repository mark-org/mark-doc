
# fields
处于不同的目的，通过不同方法索引相同的字段通常非常有用。这也是多字段的目的。
如,一个字符串字段可以映射为text字段用于全文本搜索，也可以映射为keyword字段用于排序或聚合

```
PUT my_index
{
  "mappings": {
    "_doc": {
      "properties": {
        "city": {
          "type": "text",
          "fields": {
            "raw": { 
              "type":  "keyword"
            }
          }
        }
      }
    }
  }
}
```

note：city字段用于全文本搜索。
note：city.raw用于排序与聚合。
```
GET my_index/_search
{
  "query": {
    "match": {
      "city": "york" 
    }
  },
  "sort": {
    "city.raw": "asc" 
  },
  "aggs": {
    "Cities": {
      "terms": {
        "field": "city.raw" 
      }
    }
  }
}
```





















