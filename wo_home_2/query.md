
# query DSL
https://www.elastic.co/guide/en/elasticsearch/reference/7.x/query-dsl.html

DSL(Domain Specific Language)
### two types of clauses:
* Leaf query clauses: look for a particular value in a particular field(match, term, rang)
* Compound query clauses
wrap other left or compound queries and are used to combine multiple queries in a logical fashion
(bool or dis_max) or constant_score
bool:Boolean query -> minimum_should_match 

### boost
指定一个boost值来控制每个查询子名的相对权重，默认1
