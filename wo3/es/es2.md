
# index就像关系型数据库里的database，type就像database里的table

# Index是什么
Index存储在多个分片中，其中第一个分片都是一个独立的Lucence Index.
一个大的index比多个小index效率更高：Lucene Index的固定开锁被摊分到更多文档上

另一个重要因素是你准备怎么搜索你的数据。在搜索时，每个分片都需要搜索一次。

# Type是什么
使用type允许我们在一个index里存储多种类型的数据，这样就可以减少index的数量了。
在使用时，向每个文档加入_type字段，在指定type搜索时就会被用于过滤。使用type的一个好处是，搜索一个
index下的多个type,和只搜索一个type相比没有额外的开锁--需要合并结果的分片数量是一样的。

# type限制
* 不同type里的字段需要保持一致
* 只在某个type里存在的字段，在其他没有该字段的type中也会消耗资源。
* 得分是由index内的统计数据来决定的。也就是说，一个type中的文档会影响另一个type中的文档的得分。




















