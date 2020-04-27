
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



