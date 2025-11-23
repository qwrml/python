import pytest
import allure
import sys
import os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description("Тест проверяет полный процесс оформления заказа с проверкой итоговой суммы")
def test_saucedemo_checkout():
    driver = webdriver.Chrome()
    
    try:
        with allure.step("Инициализация страниц"):
            login_page = LoginPage(driver)
            products_page = ProductsPage(driver)
            cart_page = CartPage(driver)
            checkout_page = CheckoutPage(driver)

        with allure.step("Открытие сайта магазина"):
            login_page.open("https://www.saucedemo.com/")

        with allure.step("Авторизация пользователя standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            products_page.add_product_to_cart("Sauce Labs Backpack")
            products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
            products_page.add_product_to_cart("Sauce Labs Onesie")

        with allure.step("Переход в корзину"):
            products_page.go_to_cart()

        with allure.step("Начало оформления заказа"):
            cart_page.click_checkout()

        with allure.step("Заполнение формы оформления заказа"):
            checkout_page.fill_checkout_form("John", "Doe", "12345")

        with allure.step("Проверка итоговой суммы"):
            total_amount = checkout_page.get_total_amount()
            
            with allure.step(f"Проверить что сумма ${total_amount} равна $58.29"):
                assert total_amount == "58.29"
    
    finally:
        driver.quit()