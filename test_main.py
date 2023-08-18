from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as wirewebdriver
import time


class TestForRequests:
    def calculate_visibility(self, banner_top, banner_bot, screen_height, banner_height):

        # Если баннер не видно:
        if (banner_bot < 0) or (banner_top > screen_height):
            percent_visible = 0
            return percent_visible

        else:
            visible_height = min(banner_bot, screen_height) - max(banner_top, 0)
            percent_visible = int((visible_height / banner_height) * 100)
            return percent_visible

    def test_first_request(self):
        try:
            chrome_options = Options()
            driver = wirewebdriver.Chrome(options=chrome_options)
            driver.get("https://files.adriver.ru/i.sidorovich/qat/")

            # Ждем, пока баннер прогрузится и находим его местоположение
            banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            banner_element = driver.find_element(By.TAG_NAME, "img")

            # Ждем, пока прогрузится слот для баннера и находим его
            slot_element = driver.find_element(By.ID, 'slot')

            time.sleep(4)

            # Проверяем, что был отправлен запрос на сервер
            requests = driver.requests
            for request in requests:
                if request.method == 'GET' and 'qwertytype=0' in request.url:
                    banner_request = request
                    break

            # Проверка отправки запроса
            assert 'qwertytype=0' in banner_request.url, "Request #1 wasn't send"

            # Проверка, что баннер находится в необходимом блоке
            assert banner in slot_element.find_elements(By.TAG_NAME,
                                                        "img"), "Баннер не является дочерним элементом блока с id='slot'."
            # Проверка ассертом на то, что был отправлен необходимый баннер в соответствии с требованиями
            # Запустить PyTest на все ассерты

        finally:
            time.sleep(3)
            driver.quit()

    def test_second_request_zero_visibility(self):
        try:
            chrome_options = Options()
            driver = wirewebdriver.Chrome(options=chrome_options)
            driver.get("https://files.adriver.ru/i.sidorovich/qat/")

            # Максимизировать окно браузера и проскроллить страницу до 0 видимости элемента
            driver.maximize_window()
            driver.execute_script("window.scrollBy(0, 2000);")

            # Создать экземпляр класса для вызова функции
            instance_test = TestForRequests()

            # Ждем, пока баннер прогрузится и находим его местоположение
            banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            banner_element = driver.find_element(By.TAG_NAME, "img")

            # Ждем, пока прогрузится слот для баннера и находим его
            slot_element = driver.find_element(By.ID, 'slot')

            # Получаем размеры экрана пользователя
            screen_height = driver.execute_script("return window.innerHeight")

            banner_top = driver.execute_script("return arguments[0].getBoundingClientRect().top;", banner_element)
            banner_height = driver.execute_script("return arguments[0].height;", banner_element)
            banner_bot = driver.execute_script("return arguments[0].getBoundingClientRect().bottom;", banner_element)

            # Высчитываем процент видимости баннера:
            instance_test.calculate_visibility(banner_top, banner_bot, screen_height, banner_height)

            # Проверяем, что был отправлен запрос на сервер
            time.sleep(2)
            requests = driver.requests
            for request in requests:
                if request.method == 'GET' and 'qwertytype=1' in request.url:
                    banner_request = request

                    # Пишем ассерт на проверку отправки запроса:
                    assert 'qwertytype=1' in banner_request.url, "Request #2 wasn't send"
                    break

            # Проверка, что баннер находится в необходимом блоке
            assert banner in slot_element.find_elements(By.TAG_NAME,
                                                        "img"), "Баннер не является дочерним элементом блока с id='slot'."

        finally:

            driver.quit()

    def test_second_request_from_0_to_50_visibility(self):
        try:
            chrome_options = Options()
            driver = wirewebdriver.Chrome(options=chrome_options)
            driver.get("https://files.adriver.ru/i.sidorovich/qat/")

            # Максимизировать окно браузера и проскроллить страницу до 0 видимости элемента
            driver.maximize_window()

            # Создать экземпляр класса для вызова функции
            instance_test = TestForRequests()

            # Ждем, пока баннер прогрузится и находим его местоположение
            banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            banner_element = driver.find_element(By.TAG_NAME, "img")

            # Ждем, пока прогрузится слот для баннера и находим его
            slot_element = driver.find_element(By.ID, 'slot')

            # Получаем размеры экрана пользователя
            screen_height = driver.execute_script("return window.innerHeight")

            banner_top = driver.execute_script("return arguments[0].getBoundingClientRect().top;",
                                               banner_element)
            banner_height = driver.execute_script("return arguments[0].height;", banner_element)
            banner_bot = driver.execute_script("return arguments[0].getBoundingClientRect().bottom;",
                                               banner_element)

            # Высчитываем процент видимости баннера:
            instance_test.calculate_visibility(banner_top, banner_bot, screen_height, banner_height)

            # Проверяем, что был отправлен запрос на сервер
            time.sleep(2)
            requests = driver.requests
            for request in requests:
                if request.method == 'GET' and 'qwertytype=1' in request.url:
                    banner_request = request
                    assert 'qwertytype=1' in banner_request.url, "Request #2 wasn't send"

            # Проверка, что баннер находится в необходимом блоке
            assert banner in slot_element.find_elements(By.TAG_NAME,
                                                        "img"), "Баннер не является дочерним элементом блока с id='slot'."

        finally:

            driver.quit()

    def test_second_request_more_than_50_visibility(self):
        try:
            chrome_options = Options()
            driver = wirewebdriver.Chrome(options=chrome_options)
            driver.get("https://files.adriver.ru/i.sidorovich/qat/")

            # Максимизировать окно браузера и проскроллить страницу до 0 видимости элемента
            driver.maximize_window()

            # Создать экземпляр класса для вызова функции
            instance_test = TestForRequests()
            driver.execute_script("window.scrollBy(0, 700);")

            # Ждем, пока баннер прогрузится и находим его местоположение
            banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            banner_element = driver.find_element(By.TAG_NAME, "img")

            # Ждем, пока прогрузится слот для баннера и находим его
            slot_element = driver.find_element(By.ID, 'slot')

            # Получаем размеры экрана пользователя
            screen_height = driver.execute_script("return window.innerHeight")

            banner_top = driver.execute_script("return arguments[0].getBoundingClientRect().top;",
                                               banner_element)
            banner_height = driver.execute_script("return arguments[0].height;", banner_element)
            banner_bot = driver.execute_script("return arguments[0].getBoundingClientRect().bottom;",
                                               banner_element)

            # Высчитываем процент видимости баннера:
            instance_test.calculate_visibility(banner_top, banner_bot, screen_height, banner_height)

            # Проверяем, что был отправлен запрос на сервер
            time.sleep(2)
            requests = driver.requests
            for request in requests:
                if request.method == 'GET' and 'qwertytype=1' in request.url:
                    banner_request = request
                    assert 'qwertytype=1' in banner_request.url, "Request #2 wasn't send"

            # Проверка, что баннер находится в необходимом блоке
            assert banner in slot_element.find_elements(By.TAG_NAME,
                                                        "img"), "Баннер не является дочерним элементом блока с id='slot'."


        finally:

            driver.quit()
