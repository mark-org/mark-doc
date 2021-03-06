#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/26



#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/26

import subprocess
import json
import sys




# kibana http://134.175.231.104:5601/

body_json = {
    "settings": {
            "index.number_of_shards": 1,
            "index.number_of_replicas": 0
        },
    "mappings": {
        "properties": {
            "author": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "text": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "timestamp": {
                "type": "date"
            }
        }
    }
}

body_json = json.dumps(body_json).replace("\"", "\\\"")

host = "http://134.175.231.104:9200/"

# 新增或修改_doc后面带id  _doc为type
cmd = """curl -s -H 'Content-Type:application/json;charset:utf-8' 
    -XPUT %smy_index
    -d '%s'
    | iconv -f utf-8 -t gbk
    """.replace("'", "\"") % (host, body_json)
cmd = cmd.replace("\n", "").strip()
print(cmd)

(status, output) = subprocess.getstatusoutput(cmd)
print(output)
print("-----------------end-----------------")


