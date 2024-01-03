import time

from numpy import log as ln, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://SunInJuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.implicitly_wait(10)
    x = int(browser.find_element(By.ID, "input_value").text)
    math_func = browser.find_elements(By.CLASS_NAME, "nowrap")[2].text.split()[2][:-1]
    browser.find_element(By.ID, "answer").send_keys(eval(math_func))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    alert_box = browser.switch_to.alert
    print(alert_box.text)
    alert_box.accept()
