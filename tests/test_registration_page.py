from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import helper_functions


class TestRegistration:
    def test_registration_with_correct_parameters(self, driver):
        name = helper_functions.name_generation()
        email = helper_functions.email_generation()
        password = helper_functions.password_generation()
        driver.get(Locators.page_registration_url)
        helper_functions.registration_function(name, email, password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_login_button_xpath))
        assert driver.find_element(*Locators.page_login_title).text == 'Вход'

    def test_registration_with_short_password(self, driver):
        name = helper_functions.name_generation()
        email = helper_functions.email_generation()
        password = helper_functions.short_password_generation()
        driver.get(Locators.page_registration_url)
        helper_functions.registration_function(name, email, password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_registration_error_incorrect_password))
        assert driver.find_element(*Locators.page_registration_error_incorrect_password).text == 'Некорректный пароль'
