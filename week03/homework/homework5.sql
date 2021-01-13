explain  select id,name from Table1 where name='table1'; --2 rows

create index idx_name on Table1(id,name);
show index from Table1;

explain  select id,name from Table1 where name='table1'; -- 2 rows

-- 增加索引后查询速度没有增加
/*
加索引场景
1. 数据检索时在条件字段添加索引(不在where 子句中的不适合添加索引)
2. 聚合函数对聚合字段添加索引
3. 对排序字段添加索引
4. 为了防止非聚簇索引回表查询添加索引
5. 关联查询在关联字段添加索引等
*/