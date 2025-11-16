from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")
    
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_amount(self) -> str:
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(EC.presence_of_element_located(self.total_amount))
        total_text = total_element.text
        return total_text.replace("Total: $", "")