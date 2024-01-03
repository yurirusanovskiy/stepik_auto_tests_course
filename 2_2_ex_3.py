import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    browser.find_element(By.NAME, "email").send_keys("ivan@ivanov.com")
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()
    alert_box = browser.switch_to.alert
    print(alert_box.text)
    alert_box.accept()
