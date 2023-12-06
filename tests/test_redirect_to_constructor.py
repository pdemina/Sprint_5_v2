from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
import helper_functions


class TestConstructorRedirects:
    def test_constructor_redirect_tab(self, driver):
        driver.get(Locators.page_main_url)
        driver.find_element(*Locators.page_main_button_gradient_button_xpath).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        driver.find_element(*Locators.page_main_constructor_tab_xpath).click()
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_button_gradient_button_xpath))
        assert driver.current_url == Locators.page_main_url

    def test_constructor_redirect_logo(self, driver):
        driver.get(Locators.page_main_url)
        driver.find_element(*Locators.page_main_button_gradient_button_xpath).click()
        helper_functions.login_function(Data.user_email, Data.user_password, driver)
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_name_label_xpath))
        driver.find_element(*Locators.page_main_constructor_logo_xpath).click()
        WebDriverWait(driver, 3) \
            .until(expected_conditions
                   .visibility_of_element_located(Locators.page_main_button_gradient_button_xpath))
        assert driver.current_url == Locators.page_main_url
