from numpy import log as ln, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "http://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as browser:
    browser.get(url)
    if WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")):
        browser.find_element(By.ID, "book").click()
        x = int(browser.find_element(By.ID, "input_value").text)
        math_func = [i.find_element(By.CLASS_NAME, "nowrap").text for i in
                     browser.find_elements(By.TAG_NAME, "label")][0].split()[2][:-1]
        browser.find_element(By.ID, "answer").send_keys(eval(math_func))
        browser.find_element(By.ID, "solve").click()
        alert_box = browser.switch_to.alert
        print(alert_box.text)
        alert_box.accept()
