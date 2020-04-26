#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/26

import subprocess
import json
import sys




# kibana http://134.175.231.104:5601/

body_json = {
  "query": {
    "match_all": {}
  }
}

body_json = {
  "query": {
    "match": {
      "author.keyword": "我是中国人"
    }
  }
}



body_json = json.dumps(body_json).replace("\"", "\\\"")

host = "http://134.175.231.104:9200/"

# 新增或修改_doc后面带id  _doc为type
cmd = """curl -s -H 'Content-Type:application/json;charset:utf-8' 
    -XGET %stest-index/_doc/_search?pretty
    -d '%s'
    | iconv -f utf-8 -t gbk
    """.replace("'", "\"") % (host, body_json)
cmd = cmd.replace("\n", "").strip()
print(cmd)

(status, output) = subprocess.getstatusoutput(cmd)
print(output)
print("-----------------end-----------------")


