#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/4/22

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from os import getcwd,sep


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
# browser.set_page_load_timeout(13)



# 访问
driver.get('http://192.168.101.186:9112/RedseaPlatform/skins/library/jquery/jquery.min.js')

cookie = "JSESSIONID=259D7D28EA086736DB2563CFCED99E6C; __utmv=77597140.No%20Silverlight; __utma=77597140.260084989.1502692898.1525953431.1539849996.3; rtoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODc2MDY5MTEsIlVTRVJfSUQiOiJ2L05aWUMraGZZMGhnbnpOV0dZSFNRPT0iLCJVU0VSX05BTUUiOiI4dDJNL3IzOE1HLzZNZldhcWoxQ2tnPT0iLCJpYXQiOjE1ODc2MDUxMTF9.GB-s8UIWn-Ttfde5kzt9TvmfQ_HcfqO2KbZ4T9r1CEU; LOGIN_SYS_CODE=RedseaP; redseaUserInfo=%E6%9D%8E%E6%98%8E%E4%B8%BD; CLIENT_CODE=PC; REDSESSIONID=259D7D28EA086736DB2563CFCED99E6C; LOGIN_PAGE=worktoday; LOGINTAG=5; offLineChecked=false"
c_array = cookie.split(";")

for c in c_array:
    v = c.split("=")
    driver.add_cookie({'name': v[0].strip(),'value': v[1].strip()})

driver.get('http://192.168.101.186:9112/RedseaPlatform/PtPortal.mc?method=worktoday#ajax&0&|/RedseaPlatform/worktoday/desktop.jsp?_t=1587605111593')
# 等待几秒
# wait = WebDriverWait(driver, 30) #等待的最大时间30s

# log = driver.get_log('performance')





for log in driver.get_log('performance'):
    print(log)

print(log)



# 推出驱动并关闭所关联的所有窗口
# driver.quit()