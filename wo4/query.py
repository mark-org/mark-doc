#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/26

import subprocess
import json
import sys

# kibana http://134.175.231.104:5601/

# { "price" : 1000, "color" : "红色", "brand" : "长虹", "sold_date" : "2016-10-28" }

host = "http://134.175.231.104:9200/"
# size:0表示聚合查询的结果不需要返回中间的文档内容
# buckets：存放聚合后的统计结果详细信息
# 新增或修改_doc后面带id  _doc为type
cmd = """curl -s -H 'Content-Type:application/json;charset:utf-8' 
    -XGET %stest-index/_doc/_search --data-binary @query.json
    | iconv -f utf-8 -t gbk
    """.replace("'", "\"") % (host)
cmd = cmd.replace("\n", "").strip()

print(cmd)

(status, output) = subprocess.getstatusoutput(cmd)
print(output)
print("-----------------end-----------------")
