import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_saucedemo_checkout(browser):
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

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