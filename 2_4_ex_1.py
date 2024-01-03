from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/cats.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    # browser.implicitly_wait(5)
    browser.find_element(By.ID, "button").click()