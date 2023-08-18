from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSelenium:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def get_button(self):
        try:
            self.driver.get("https://aleftina17.github.io/cherry-blossom-shop/")
            self.driver.maximize_window()
            # button = self.wait.until(EC.presence_of_element_located((By.ID, "submit_button")))
            button = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "container")))#.find_elements(By.CLASS_NAME, "container")

        finally:
            # assert button == "Submit"
            for but in button:
                print(but.text)

            self.driver.quit()


test123 = TestSelenium()

test123.get_button()
