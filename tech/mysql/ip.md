
# 找出连接IP
select SUBSTRING_INDEX(host,':',1) as ip , count(*) from information_schema.processlist group by ip;