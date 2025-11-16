import pytest
import allure
import time
import sys
import os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.calculator_page import CalculatorPage

@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка калькулятора с задержкой 45 секунд")
@allure.description("Тест проверяет вычисление 7+8 с задержкой 45 секунд")
def test_slow_calculator():
    driver = webdriver.Chrome()
    
    try:
        with allure.step("Создание страницы калькулятора"):
            calculator = CalculatorPage(driver)
        
        with allure.step("Открытие страницы калькулятора"):
            calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        with allure.step("Установка задержки 45 секунд"):
            calculator.set_delay(45)
        
        with allure.step("Ввод выражения 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")
        
        with allure.step("Ожидание и проверка результата"):
            start_time = time.time()
            result = calculator.get_result()
            end_time = time.time()
            
            execution_time = end_time - start_time
            
            with allure.step(f"Проверить результат {result} и время выполнения {execution_time:.2f}сек"):
                assert result == "15"
                assert execution_time >= 45
    
    finally:
        driver.quit()