import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys

# url = "https://www.amazon.com"
url = 'http://httpbin.org/ip'
# proxy_host = "proxy.crawlera.com"
# proxy_port = "8010"
# proxy_auth = "e0487c83dd6f444a9f9df543f8a461d6:" # Make sure to include ':' at the end
# proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#       "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

# r = requests.get(url, proxies=proxies, verify=False)

# print("""
# Requesting [{}]
# through proxy [{}]

# Request Headers:
# {}

# Response Code: {}
# {}

# """.format(url, proxy_host, r.request.headers, r.status_code, r.text))
PROXY = "https://e0487c83dd6f444a9f9df543f8a461d6@proxy.crawlera.com:8010/"
proxy = Proxy()
proxy.HttpProxy = "http://e0487c83dd6f444a9f9df543f8a461d6@proxy.crawlera.com:8010/"
proxy.SslProxy = "127.0.0.1:3330"


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=%s' % PROXY)
chromeOptions.add_argument("ignore-certificate-errors")

chromeOptions.Proxy = proxy

driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)