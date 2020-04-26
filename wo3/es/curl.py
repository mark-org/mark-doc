#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/26

import subprocess
import json

# kibana http://134.175.231.104:5601/

body_json = {
    "name": "OK1"
}

body_json = json.dumps(body_json).replace("\"", "\\\"")

# 新增或修改_doc后面带id  _doc为type
cmd = """curl -s -H 'Content-Type:application/json;charset:utf-8' 
    -XPUT http://134.175.231.104:9200/test-indexx/docx/new_002
    -d '%s'
    """.replace("'", "\"") % body_json
cmd = cmd.replace("\n", "").strip()
print(cmd)

(status, output) = subprocess.getstatusoutput(cmd)
print(output)
print("-----------------end-----------------")
