from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestTabsSwitching:
    def test_souses_opening(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.page_main_souces).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.page_main_souce_selected))
        assert driver.find_element(*Locators.page_main_check_tab_souces).get_attribute("class") == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


    def test_filler_opening(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.page_main_fillers).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.page_main_filler_selected))
        assert driver.find_element(*Locators.page_main_check_tab_fillers).get_attribute("class") == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_go_to_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.page_main_souces).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.page_main_souce_selected))
        driver.find_element(*Locators.page_main_buns).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.page_main_buns_selected))
        assert driver.find_element(*Locators.page_main_check_tab_buns).get_attribute("class") == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

