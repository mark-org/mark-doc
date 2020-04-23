#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/22

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from os import getcwd,sep
import time


options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
# options.add_argument('--headless')
options.add_argument('--disable-gpu')


caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}

driver = webdriver.Chrome(desired_capabilities=caps)
# 当前进程的工作目录
# 设置超时时间
driver.set_page_load_timeout(10)



# 访问
driver.get('http://192.168.101.244:8199/RedseaPlatform/')
# driver.get('http://192.168.101.186:9112/RedseaPlatform/')

# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "footTextColor")))

value2 = driver.execute_script("return pubAesEncrypt('123','ps_uer_!@#BGYUJN')")

print(value2)

# print(driver.page_source)

t1 = time.time()
if '"" == "ps_uer_!@#BGYUJN"' in driver.page_source:
    print("no ...")
else:
    print("yes ...")
print(time.time() - t1)


# 推出驱动并关闭所关联的所有窗口
driver.quit()