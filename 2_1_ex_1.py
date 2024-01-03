from numpy import log as ln, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://suninjuly.github.io/math.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    x = int(browser.find_element(By.ID, "input_value").text)
    math_func = browser.find_elements(By.CLASS_NAME, "nowrap")[2].text.split()[2][:-1]
    browser.find_element(By.ID, "answer").send_keys(eval(math_func))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
