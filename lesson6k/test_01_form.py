from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Edge()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров", 
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
        }
        
    for field_id, value in form_data.items():
        field = driver.find_element(By.ID, field_id)
        field.clear()
        field.send_keys(value)
        
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
        
    wait = WebDriverWait(driver, 10)
        
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
        )
    zip_code_classes = zip_code_field.get_attribute("class")
    assert "is-invalid" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"
        
    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
        ]
        
    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "is-valid" in field_classes, f"Поле {field_id} должно быть подсвечено зеленым"
    
    driver.quit()