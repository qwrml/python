from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
    
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    
input_field.send_keys("Sky")
sleep(3)
    
input_field.clear()
sleep(3)
    
input_field.send_keys("Pro")
sleep(3)

driver.quit()