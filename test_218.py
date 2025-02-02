from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn1 = browser.find_element(By.ID, "book")
    btn1.click()

    ans = calc(int(browser.find_element(By.ID, "input_value").text))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(ans)

    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

finally:
    time.sleep(60)
    browser.quit()
