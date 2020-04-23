#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/22

# kibana_sample_data_ecommerce

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://134.175.231.104:9200/'])

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", id=1, body=doc)
# print(res['result'])
#
# res = es.get(index="test-index", id=1)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")

# customer_first_name：Eddie，Mary， Gwen

query_string = {"query": "中国"}

bool = {"filter":{"query_string":query_string}}
res = es.search(index="test-index", body={"query": {"bool": bool}})
print(res)

print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit["_source"])



print("------------------------------end-----------------------------")

