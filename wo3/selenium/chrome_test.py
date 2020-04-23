#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/22

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from os import getcwd,sep
import json


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# options = webdriver.ChromeOptions()
# # 使用headless无界面浏览器模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')



caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        # 'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL'
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
            'enablePage': False
        },
        'w3c': False,
        'args': ['--headless', '--disable-gpu']
    },
}




# options.set_capability("loggingPrefs", {'performance': 'ALL'})
# options.set_capability("goog:chromeOptions", prefs)



driver = webdriver.Chrome(desired_capabilities=caps)
# 当前进程的工作目录
# 设置超时时间
# browser.set_page_load_timeout(13)
#






# 等待几秒
# wait = WebDriverWait(driver, 30) #等待的最大时间30s

# log = driver.get_log('performance')

# 去掉favicon.ico:1 GET http://127.0.0.1:5000/favicon.ico 404 (NOT FOUND)

driver.get('http://127.0.0.1:5000/static/test.js')
driver.get_log('performance')
driver.get_log('browser')
print("begin........................")

driver.get('http://127.0.0.1:5000/static/test.html')


# 控制台 browser
for log in driver.get_log('performance'):
    message = json.loads(log['message'])['message']
    if message['method'] == "Network.responseReceived":
        print(message)
        url = message["params"]["response"]["url"]
        status = message["params"]["response"]["status"]
        if url.endswith("favicon.ico"):
            continue
        print(url, status)

# {'level': 'SEVERE', 'message': 'http://127.0.0.1:5000/favicon.ico - Failed to load resource:
for log in driver.get_log('browser'):
    print(log)





#
# print(log)

# {'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived



print("end")


# 推出驱动并关闭所关联的所有窗口
driver.quit()