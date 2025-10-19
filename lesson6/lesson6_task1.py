from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.ID, "ajaxButton")
button.click()
    
wait = WebDriverWait(driver, 15)
message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
    
print(message.text)

driver.quit()