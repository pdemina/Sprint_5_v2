from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators
from faker import Faker


def login_function(email, password, driver):
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Locators.field_email_xpath))
    driver.find_element(*Locators.field_email_xpath).send_keys(Data.user_email)
    driver.find_element(*Locators.field_password_xpath).send_keys(Data.user_password)
    driver.find_element(*Locators.page_login_button_xpath).click()


def name_generation():
    fake = Faker()
    name = fake.name()
    return name


def email_generation():
    fake = Faker()
    email_first_part = fake.pystr()
    email_first_part = email_first_part[:7]
    email = email_first_part + "@gmail.com"
    return email


def password_generation():
    fake = Faker()
    password = fake.pystr()
    password = password[:6]
    return password


def short_password_generation():
    fake = Faker()
    password = fake.pystr()
    password = password[:5]
    return password


def registration_function(name, email, password, driver):
    WebDriverWait(driver, 3) \
        .until(expected_conditions
               .visibility_of_element_located(Locators.page_registration_register_button))
    driver.find_element(*Locators.page_registration_name_field).send_keys(name)
    driver.find_element(*Locators.page_registration_email_field).send_keys(email)
    driver.find_element(*Locators.page_registration_password_field).send_keys(password)
    driver.find_element(*Locators.page_registration_register_button).click()

