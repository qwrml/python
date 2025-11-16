from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ProductsPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.product_add_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
    
    def add_product_to_cart(self, product_name: str) -> None:
        self.driver.find_element(*self.product_add_buttons[product_name]).click()
    
    def go_to_cart(self) -> None:
        self.driver.find_element(*self.shopping_cart).click()