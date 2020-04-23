from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from flask import Flask
import json

app = Flask(__name__)


class Static(object):
    driver = None


@app.route('/')
def hello_world():

    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

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
            'args': ['-id000001']
        }
    }

    if Static.driver is None:
        driver = webdriver.Chrome(desired_capabilities=caps)
        Static.driver = driver
    else:
        driver = Static.driver

    mainUrl = "http://127.0.0.1:5000/static/test.html"
    # try:
    #     #
    #     driver.refresh()
    #     # driver.get(mainUrl)
    #     # driver.get_log('performance')
    # except SyntaxError as e:
    #     print("eeeeeee")
    #     print("xxx:%s" % e.args)
    #     if "chrome not reachable" in e.args:
    #         driver = webdriver.Chrome(desired_capabilities=caps)
    #         Static.driver = driver
    #     else:
    #         print(e)
    #         return "error...."

    driver.get(mainUrl)
    for log in driver.get_log('performance'):
        message = json.loads(log['message'])['message']
        if message['method'] == "Network.responseReceived":
            print(message)
            url = message["params"]["response"]["url"]
            status = message["params"]["response"]["status"]
            if url.endswith("favicon.ico"):
                continue
            print(url, status)
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
