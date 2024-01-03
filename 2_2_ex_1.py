import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://suninjuly.github.io/selects1.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    l = [i.text for i in browser.find_elements(By.TAG_NAME, "span")][3:]
    res = str(eval(" ".join(l)))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res)
    browser.find_element(By.CLASS_NAME, "btn").click()
    alert_box =  browser.switch_to.alert
    print(alert_box.text)
    alert_box.accept()
