from numpy import log as ln, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/redirect_accept.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.implicitly_wait(10)
    x = int(browser.find_element(By.ID, "input_value").text)
    math_func = [i.find_element(By.CLASS_NAME, "nowrap").text for i in
                 browser.find_elements(By.TAG_NAME, "label")][0].split()[2][:-1]

    browser.find_element(By.ID, "answer").send_keys(eval(math_func))
    browser.find_element(By.TAG_NAME, "button").click()
    alert_message = browser.switch_to.alert
    print(alert_message.text)
    alert_message.accept()
