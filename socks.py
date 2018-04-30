from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.proxy import *
service_args = [
        '--ignore-ssl-errors=true',
        '--ssl-protocol=all',
        '--proxy=59.62.3.183:14800',
        '--proxy-type=socks5',
        ]
myProxy = "59.62.3.183:14800"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })
driver = webdriver.Firefox(executable_path=r'E:\pythonPars\geck\geckodriver.exe', service_args=service_args)
driver.get('https://2ip.ru/')	

