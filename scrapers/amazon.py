print('importing libraries...')
import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from dhooks import Webhook, Embed

def hook_send(product_url, stock):
    print(product_url)
    hook = Webhook(
        "https://discordapp.com/api/webhooks/697993898659676230/09E2-tTgtVWc6NLuJ5NgaXyioE98A_VADBR3MbULkupaz-C_1UDX350L2VEDV46ams07"
    )
    embed = Embed(description=product_url, color=0x5CDBF0, timestamp="now")
    embed.add_field(name="STOCK AVAILABILITY", value=stock)
    hook.send(embed=embed)

options = webdriver.ChromeOptions()  
options.add_argument('headless')
desired_caps = options.to_capabilities()

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "http://scraperapi.country_code=us:1b7080951f89c7feca19ad9801aed691@proxy-server.scraperapi.com:8001"
# prox.https_proxy = "https://scraperapi.country_code=us:1b7080951f89c7feca19ad9801aed691@proxy-server.scraperapi.com:8001"
prox.https_proxy = "https://e0487c83dd6f444a9f9df543f8a461d6@proxy.crawlera.com:8010/"
prox.http_proxy = "http://e0487c83dd6f444a9f9df543f8a461d6@proxy.crawlera.com:8010/"
prox.add_to_capabilities(desired_caps)
driver = webdriver.Chrome(desired_capabilities=desired_caps)

url = 'https://www.amazon.com'
driver.get(url)

try:
    address_xpath = '//*[@id="nav-main"]/div[1]/div[2]/div/div[3]/span[2]/span/input'
    address = driver.find_element_by_xpath(address_xpath)
except:
    address = None

if address:
    print('checking address...')
    driver.find_element_by_xpath(address_xpath).click()
    time.sleep(2)

    bar_xpath = '//*[@id="GLUXZipUpdateInput"]'
    bar = driver.find_element_by_xpath(bar_xpath)
    bar.send_keys('75001')
    bar.send_keys(Keys.ENTER)
    time.sleep(3)

    # click continue button
    con = '//*[@id="a-popover-3"]/div/div[2]/span'
    driver.find_element_by_xpath(con).click()
    time.sleep(2)

urls = ['https://www.amazon.com/gp/offer-listing/B07VGRJDFY', 'https://www.amazon.com/gp/offer-listing/B07GH953JN', 'https://www.amazon.com/gp/offer-listing/B07XLGBYM3', 'https://www.amazon.com/gp/offer-listing/B085TFF7M1', 'https://www.amazon.com/gp/offer-listing/B084Y3VVNG', 'https://www.amazon.com/gp/offer-listing/B07SW925DR', 'https://www.amazon.com/gp/offer-listing/B07SXF8GY3', 'https://www.amazon.com/gp/offer-listing/B07SRVTV6X', 'https://www.amazon.com/gp/offer-listing/B00NB3P98G/', 'https://www.amazon.com/gp/offer-listing/B001U5SPHY']

# scraping amazon product links
pause_count = 0
while True:
    count = 1
    for url in urls:
        print('checking product {}'.format(count))
        driver.get(url)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        try:
            seller = soup.find('h3', class_='a-spacing-none olpSellerName').find('img')['alt']
        except:
            seller = None
        if seller == 'Amazon.com':
            stock = 'IN STOCK'
            print(stock)
            hook_send(url, stock)
        else:
            stock = 'OUT OF STOCK'
            print(stock)
            # hook_send(url, stock)
        
        count += 1
        time.sleep(2)

    # sleep for 3 seconds before running again
    print("3 second wait...")
    time.sleep(3)
    print()

    pause_count += 1
    if pause_count % 8 == 0:
        print("Ten minutes pause...")
        time.sleep(600)


driver.quit()
print("Monitoring completed!")