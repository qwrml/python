from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
    
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")
    
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")
    
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
    
sleep(2)
    
success_message = driver.find_element(By.ID, "flash")
    
print("Текст сообщения:", success_message.text)
    
sleep(2)

driver.quit()