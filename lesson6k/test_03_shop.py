from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_purchase():
    driver = webdriver.Firefox()
    
    driver.get("https://www.saucedemo.com/")
        
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
        
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
        
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Onesie"
        ]
        
    for product_name in products_to_add:
        add_button = driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        add_button.click()
        
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
        
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
        
    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    postal_code_field = driver.find_element(By.ID, "postal-code")
        
    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Петров")
    postal_code_field.send_keys("123456")
        
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
        
    wait = WebDriverWait(driver, 10)
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
    total_text = total_element.text
    total_amount = total_text.replace("Total: $", "")
        
    assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получили ${total_amount}"
        
    print(f"Итоговая сумма: ${total_amount}")
        
    driver.quit()