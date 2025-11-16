from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
    
    def click_checkout(self) -> None:
        self.driver.find_element(*self.checkout_button).click()