import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.implicitly_wait(10)

driver.get("https://files.adriver.ru/i.sidorovich/qat/")   # Скрипт не улавливает нужный запрос, нужно верно выставить время ожидания запроса

banner = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "img")))


for request in driver.requests:
    if request.response:
        print(request.url)

url = "https://34b81d49-1c76-4a3e-8e8f-73deea0b714b.mock.pstmn.io"

assert request.url == url, "URL is wrong" # здесь проверить, что отправляемый УРЛ соответствует ТЗ