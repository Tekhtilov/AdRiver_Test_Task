import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("http://suninjuly.github.io/selects1.html")

num1 = wait.until(EC.visibility_of_element_located((By.ID, 'num1'))).text
num2 = wait.until(EC.visibility_of_element_located((By.ID, 'num2'))).text

num3 = int(num1) + int(num2)

select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(num3))

button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn'))).click()

alert = wait.until(EC.alert_is_present()).text.split()


new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

time.sleep(1)
# print(alert[-1])


