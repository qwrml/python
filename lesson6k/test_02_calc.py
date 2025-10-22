from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome()
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")
        
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()  
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
        
    wait = WebDriverWait(driver, 46)
    result = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        
    screen = driver.find_element(By.CLASS_NAME, "screen")
    assert screen.text == "15", f"Результат: {screen.text}, ожидалось: 15"
        
    driver.quit()