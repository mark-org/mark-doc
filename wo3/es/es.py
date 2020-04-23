#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/22

from datetime import datetime
from elasticsearch import Elasticsearch

# es = Elasticsearch(['https://user:secret@localhost:443'])
es = Elasticsearch(['http://134.175.231.104:9200/'])

id = 12
doc = {
    'author': '我是中国人',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=id, body=doc)
print(res['result'])

res = es.get(index="test-index", id=id)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])



print(1)