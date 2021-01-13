/*MYSQL@5.7*/
-- 修改密码
ALTER USER 'rooy'@'localhost' IDENTIFIED BY 'new_password'


-- 查看密码复杂度
show variables like 'validate_password%';

-- 修改密码强度
set global validate_password_policy='LOW'; --或者=0

-- 查看默认字符集
show variables like '%character%';

--修改字符集；utf8 不是UTF-8字符集
set global character_set_server=utf8mb4;
set global character_set_database=utf8mb4;
set global character_set_client=utf8mb4;
set global character_set_connection=utf8mb4;

-- 查看校对规则 --utf8mb4_0900_ai_ci    _ci大小写不敏感 _cs大小写敏感
show variables like 'collation_%'; 



/*增加远程用户*/
# mysql -u root -p --(输入密码)
>>use mysql
>>grant all privileges on *.* to 'test'@"%" identified by "password";  
flush privileges;   * 刷新刚才的内容*

-- 为现有用户添加远程访问权限：
select  User,Host from user
update db set host = '%' where user = '用户名'; --（如果写成 host=localhost 那此用户就不具有远程访问权限）
flush privileges;
