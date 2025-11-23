Проект автотестов Lesson 10

Запуск тестов для формирования отчета

# Запуск теста калькулятора с генерацией Allure результатов
pytest tests/test_calculator.py --alluredir=allure-results

# Запуск теста интернет-магазина с генерацией Allure результатов  
pytest tests/test_saucedemo.py --alluredir=allure-results

# Запуск всех тестов с генерацией Allure результатов
pytest tests/ --alluredir=allure-results