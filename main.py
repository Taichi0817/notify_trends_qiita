from selenium import webdriver
import time
import pandas as pd
import requests
from assets import line_notify


browser = webdriver.Chrome('/Users/gleek908i/Downloads/chromedriver')
browser.get('https://qiita.com')

res = []
for elem_a in browser.find_elements_by_xpath('//h2/a'):
    elem_h2 = elem_a.find_element_by_xpath('..')
    res1 = elem_a.text + '\n'
    res2 = elem_a.get_attribute('href') + '\n'
    res.append(res1)
    res.append(res2)

line_notify.send_line(res)