import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для вычисления процента видимости баннера
def calculate_percent_visible(banner_element):
    # Проверяем, видим ли элемент на странице
    if banner_element.is_displayed():
        # Если элемент видим, возвращаем 100%
        return 100
    else:
        # Если элемент невидим, возвращаем 0%
        return 0

# Запуск браузера
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

# Переход на тестовую страницу
driver.get("https://files.adriver.ru/i.sidorovich/qat/")

# Ждем, пока баннер отобразится на странице (timeout=10 секунд)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))

# Получаем элемент баннера
banner_element = driver.find_element(By.TAG_NAME, "img")

# Максимизируем окно браузера для точных вычислений координат
driver.maximize_window()

# driver.execute_script("window.scrollBy(0, 300);")
time.sleep(5.5)


# Получаем размеры экрана пользователя
screen_width = driver.execute_script("return window.innerWidth")
screen_height = driver.execute_script("return window.innerHeight")


banner_top = driver.execute_script("return arguments[0].getBoundingClientRect().top;", banner_element)
banner_height = driver.execute_script("return arguments[0].height;", banner_element)
banner_bot = driver.execute_script("return arguments[0].getBoundingClientRect().bottom;", banner_element)



print("Расстояние до верхняя точка баннера", banner_top)
print("Высота баннера", banner_height)
print("Расстояние до нижняя точка баннера", banner_bot)
print("Высота экрана", screen_height)


def obosranaya_func(banner_top, banner_bot, screen_height, banner_height):

    # Если не видно:
    if (banner_bot < 0) or (banner_top > screen_height):
        print(f'0%')

    else:
        visible_height = min(banner_bot, screen_height) - max(banner_top, 0)
        percent_visible = int((visible_height / banner_height) * 100)
        print(f"percentage of banner visibility = {percent_visible}%")


obosranaya_func(banner_top, banner_bot, screen_height, banner_height)




driver.quit()
