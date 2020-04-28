
# DSL查询存在两种
* query DSL 和 filter DSL
### query DSL
“这个文档匹不匹配这个查询，它的相关度高么？”
ES中索引的数据都会存储一个_score分值，分值越高就代表越匹配'
一些query的场景
* 与full text search的匹配度最高
* 包含run单词，如果包含有这些单词：runs、running、job、sprint，也被视为包含run单词
* 包含quick、brown、fox.这些词越接近，这份文档的相关性就越高
### filter DSL
“这个文档匹不匹配？”
它不会去计算任何分值，也不会关心返回的排序问题，因些效率会高一点。
用在bool查询中，使用must_not或者filter
* 另外，经常使用过滤器，ES会自动的缓存过滤器的内容，这对于查询来说，会提交很多性能
一些过滤的情况：
* 创建日期是否在2013-2014年间?
* status字段是否为published?
* lat_lon字段是否在某个坐标的10公里范围内？


# dis_max查询(Disjunction Max Query:分离最大化查询)
* 将任何与任一查询匹配的文档作为结果返回，但只将最佳匹配的评分作为查询的评分结果返回












































