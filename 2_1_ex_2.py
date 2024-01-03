from numpy import log as ln, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

url = " http://suninjuly.github.io/get_attribute.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    x = int(browser.find_element(By.ID, "treasure").get_attribute("valuex"))
    print(x)
    math_func = browser.find_elements(By.CLASS_NAME, "nowrap")[2].text.split()[2][:-1]
    print(math_func)
    browser.find_element(By.ID, "answer").send_keys(eval(math_func))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    alert_box = browser.switch_to.alert
    print(alert_box.text)
    alert_box.accept()
