import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://suninjuly.github.io/get_attribute.html")

x = wait.until(EC.visibility_of_element_located((By.ID, 'treasure'))).get_attribute("valuex")
y = calc(x)

inputtt = wait.until(EC.visibility_of_element_located((By.ID, 'answer'))).send_keys(y)

checkbox = wait.until(EC.visibility_of_element_located((By.ID, "robotCheckbox"))).click()
radio = wait.until(EC.visibility_of_element_located((By.ID, 'robotsRule'))).click()
button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn'))).click()

alert = wait.until(EC.alert_is_present()).text.split()

print(alert[-1])


# assert people_checked is None, "People radio is not selected by default"



time.sleep(3)