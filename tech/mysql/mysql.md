

# mysql-derived 派生表
* set optimizer_switch='derived_merge=on'; set optimizer_switch='derived_merge=off';
* 什么是派生表derived?
>> * 子查询-->在From后where前的子查询
explain select * from (select * from t) a where id = 2;
>> * 1.执行select * from t 2.子查询结果写到临时表a 3.回读id = 2

* MySQL 5.7开始优化器引入derived_merge，可以理解为Oracle的子查询展开，
有优化器参数optimizer_switch='derived_merge=ON’来控制，默认为打开。

* 注:
但是仍然有很多限制，当派生子查询存在以下操作时该特性无法生效：UNION 、GROUP BY、DISTINCT、LIMIT/OFFSET以及聚合操作

```sql
explain select * from (SELECT * FROM repository.auth_res) where res_id = 1
-- Error Code: 1248. Every derived table must have its own alias

explain select * from (SELECT * FROM repository.auth_res limit 100) t where res_id = 1
1	PRIMARY	<derived2>		ref	<auto_key0>	<auto_key0>	4	const	1	100.00	
2	DERIVED	auth_res		ALL					6	100.00	

```

# 执行计划
const, system: 单表中最多有一个匹配行，查询起来非常迅速，例如根据主键或唯一索引查询

explain select * from auth_res r
	where exists (select 1 from auth_res where res_id = 1 and res_id = r.res_id)

explain select * from auth_res r
	join auth_res rr on rr.res_id = 1 and rr.res_id = r.res_id


