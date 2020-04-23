#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/10


import requests
import time
import hashlib
import commands
import os

# j_username = "系统管理员"
# j_password = "Loe/YCaeIJPFa4h/GsUl7w=="

j_username = "系统管理员"
j_password = "Loe/YCaeIJPFa4h/GsUl7w=="
url = "http://jjhr.sunriver.cn:8082/RedseaPlatform/j_red_security_check/PW"

# url = "http://192.168.101.244:8199/RedseaPlatform/j_red_security_check/PW"

data =  {"j_username": j_username, "j_password": j_password}
timestamp = "%s000" % (int(time.time()))

timestamp = "2586506794788"

init_pw = "123456jj"
v = "%s!@#$%%%s%s" % (j_username, init_pw, timestamp)
print v
md5 = hashlib.md5(v).hexdigest().upper()
print md5
md5 = "8F2C8B05D99FC560B077026263D4CAD8"

headers = \
    {
        "testToken": md5,
        "timestamp": timestamp,
        "Host": "jjhr.sunriver.cn:8082",
        "Cookie": "LOGIN_SYS_CODE=RedseaP",
        "X-Requested-With": "XMLHttpRequest"
    }
try:
    res = requests.post(url=url, headers=headers, data=data,  timeout=5)
    print res.headers["Set-Cookie"]
    print(res.text)

    # url = "http://jjhr.sunriver.cn:8082/RedseaPlatform/getList/pt_menu_checklist/CoreRequest.mc?root_id=gourgen"
    # headers = \
    #     {
    #         "Host": "jjhr.sunriver.cn:8082",
    #         "Cookie": res.headers["Set-Cookie"],
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    # res = requests.post(url=url, headers=headers, data=data, timeout=5)
    # print(res.text)
    test_url = "http://jjhr.sunriver.cn:8082/RedseaPlatform/PtPortal.mc?method=classic#ajax&1&nworktoday-40175-24311-22537-13403&|RedseaPlatform/PtMenu.mc?method=commonOrgTree&command=/RedseaPlatform/hrRoster/0fc0bf11-332f-11e8-805c-801844e4b018/getCustomCommonList.mc?param=struTreeCode,struId,rootId,belongUnitStruId&tableId=9eaf2c17635d42d8ac4b700fcce79f9b&ptType=1&_t=1586499721201&menuName=%E8%AF%81%E4%BB%B6%E7%AE%A1%E7%90%86"

    cmd = "D:/Java7/jdk1.7.0_80/bin/phantomjs.exe E:/python/myproject/deploy/check/menu/scan_url.js \"%s\" \"%s\" %s" % \
                                                (res.headers["Set-Cookie"], test_url, "jjhr.sunriver.cn")
    # (status, output) = commasnds.getstatusoutput("ls")
    begin = time.time()
    output = os.system(cmd)
    print "spend time:%s" % (time.time() - begin)
    print cmd
    print "begin"

    # print status
    print output.decode("gbk")
    print "end"


except requests.exceptions.RequestException as e:
    print(e)


