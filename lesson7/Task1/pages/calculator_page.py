from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[text()='{}']"
    
    def open(self, url):
        self.driver.get(url)
    
    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
    def click_button(self, button_text):
        locator = (By.XPATH, self.button_locator.format(button_text))
        button_element = self.driver.find_element(*locator)
        button_element.click()
    
    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: driver.find_element(*self.result_display).text != ""
        )
        return self.driver.find_element(*self.result_display).text