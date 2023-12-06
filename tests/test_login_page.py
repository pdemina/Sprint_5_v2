from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
import helper_functions


class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(Locators.page_main_url)
        driver.find_element(*Locators.page_main_button_gradient_button_xpath).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        assert driver.find_element(*Locators.page_main_button_gradient_button_xpath).text == "Оформить заказ"

    def test_login_from_personal_account(self, driver):
        driver.get(Locators.page_main_url)
        driver.find_element(*Locators.page_main_personal_account_tab_xpath).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        assert driver.current_url == Locators.page_main_url

    def test_login_from_registration_page(self, driver):
        driver.get(Locators.page_registration_url)
        driver.find_element(*Locators.page_registration_enter_button).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        assert driver.find_element(*Locators.page_main_button_gradient_button_xpath).text == "Оформить заказ"

    def test_login_from_forgot_password_page(self, driver):
        driver.get(Locators.page_forgot_password_url)
        driver.find_element(*Locators.page_forgot_password_enter_button).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        assert driver.find_element(*Locators.page_main_button_gradient_button_xpath).text == "Оформить заказ"

