from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
    
    def open(self, url: str) -> None:
        self.driver.get(url)
    
    def set_delay(self, delay_value: int) -> None:
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))
    
    def click_button(self, button_text: str) -> None:
        if button_text == "+":
            locator = (By.XPATH, "//span[text()='+']")
        elif button_text == "=":
            locator = (By.XPATH, "//span[text()='=']")
        else:
            locator = (By.XPATH, f"//span[text()='{button_text}']")
        
        button_element = self.driver.find_element(*locator)
        button_element.click()
    
    def get_result(self, timeout: int = 50) -> str:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: driver.find_element(*self.result_display).text != "7+8"
        )
        return self.driver.find_element(*self.result_display).text