import pytest
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.calculator_page import CalculatorPage

def test_slow_calculator(browser):
    calculator = CalculatorPage(browser)
    calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator.set_delay(45)

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    start_time = time.time()
    result = calculator.get_result()
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    assert result == "15"
    assert execution_time >= 45