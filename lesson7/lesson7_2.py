from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def open(self, url):
        self.driver.get(url)
    
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.product_add_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
    
    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.product_add_buttons[product_name]).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
    
    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def get_total_amount(self):
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(EC.presence_of_element_located(self.total_amount))
        total_text = total_element.text
        return total_text.replace("Total: $", "")

driver = webdriver.Chrome()

login_page = LoginPage(driver)
products_page = ProductsPage(driver)
cart_page = CartPage(driver)
checkout_page = CheckoutPage(driver)

login_page.open("https://www.saucedemo.com/")
login_page.login("standard_user", "secret_sauce")

products_page.add_product_to_cart("Sauce Labs Backpack")
products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
products_page.add_product_to_cart("Sauce Labs Onesie")

products_page.go_to_cart()
cart_page.click_checkout()
checkout_page.fill_checkout_form("John", "Doe", "12345")

total_amount = checkout_page.get_total_amount()
assert total_amount == "58.29"

driver.quit()