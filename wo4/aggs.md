
# 
* elasticsearch7默认不在支持指定索引类型，默认索引类型是_doc，
```
"mappings": {
	"properties": {
		"price": {
			"type": "long"
		},
		"color": {
			"type": "keyword"
		},
		"brand": {
			"type": "keyword"
		},
		"sold_date": {
			"type": "date"
		}
	}
}
```






















