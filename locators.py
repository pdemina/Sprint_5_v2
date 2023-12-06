from selenium.webdriver.common.by import By


class Locators:
    # section below with variables for login page:
    page_login_url = 'https://stellarburgers.nomoreparties.site/login' # url страницы логин
    page_login_title = By.XPATH, ".//h2[(text() = 'Вход')]"
    field_email_xpath = By.XPATH, ".//input[(@class = 'text input__textfield text_type_main-default' and @type='text')]"  # email поле
    field_password_xpath = By.XPATH, ".//input[(@class = 'text input__textfield text_type_main-default' and @type='password')]"  # password поле
    page_login_button_xpath = By.XPATH, ".//button[text()='Войти']"  # кнопка войти
    page_login_registration_link = By.XPATH, ".//a[(@class = 'Auth_link__1fOlj')]"  # ссылка Зарегестрироваться
    # main page:
    page_main_url = "https://stellarburgers.nomoreparties.site/"  # url главной страницы Конструктор
    page_main_button_gradient_button_xpath = By.XPATH, ".//button[(@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg')]"
    page_main_name_label_xpath = By.XPATH, ".//h1[text()='Соберите бургер']"  # заголовок страницы "Соберите бургер"
    page_main_personal_account_tab_xpath = By.XPATH, ".//p[text()='Личный Кабинет']" # вкладка Личный кабинет
    page_main_constructor_tab_xpath = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"  # вкладка Конструктор
    page_main_constructor_logo_xpath = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"  # лого
    page_main_souces = By.XPATH, './/span[text()="Соусы"]' #для клика по вкладке Соусы
    page_main_fillers = By.XPATH, './/span[text()="Начинки"]' #для клика по вкладке Начинки
    page_main_buns = By.XPATH, './/span[text()="Булки"]'#для клика по вкладке Булки
    page_main_check_tab_souces = By.XPATH, ".//span[text()='Соусы']/parent::div" #для вытаскивания класса для assert вкладки Соусы
    page_main_check_tab_fillers = By.XPATH, ".//span[text()='Начинки']/parent::div" #для вытаскивания класса для assert вкладки Начинки
    page_main_check_tab_buns = By.XPATH, ".//span[text()='Булки']/parent::div" #для вытаскивания класса для assert вкладки Булки
    page_main_souce_selected=By.XPATH,".//span[text()='Соусы']/parent::div[contains(@class,'tab_tab_type_current')]" #для ожидания переключения класса
    page_main_filler_selected = By.XPATH, ".//span[text()='Начинки']/parent::div[contains(@class,'tab_tab_type_current')]" #для ожидания переключения класса
    page_main_buns_selected = By.XPATH, ".//span[text()='Булки']/parent::div[contains(@class,'tab_tab_type_current')]" #для ожидания переключения класса
    # registration page:
    page_registration_url = "https://stellarburgers.nomoreparties.site/register"  # url регистрации
    page_registration_enter_button = By.XPATH, ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]"  # кнопка - войти
    page_registration_error_not_unique_user = By.XPATH, ".//p[text()='Такой пользователь уже существует']"
    page_registration_error_incorrect_password = By.XPATH, ".//p[text()='Некорректный пароль']"
    page_registration_name_field = By.XPATH, ".//fieldset[1]//input"
    page_registration_email_field = By.XPATH, ".//fieldset[2]//input"
    page_registration_password_field = By.XPATH, ".//fieldset[3]//input"
    page_registration_register_button = By.XPATH, ".//button[(@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')]"  # кнопка Зарегистрироваться
    # forgot password page:
    page_forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password"  # url восстановление пароля
    page_forgot_password_enter_button = By.XPATH, ".//a[(@class = 'Auth_link__1fOlj' and text()='Войти')]"  # кнопка - войти
    #personal account page
    page_personal_account = "https://stellarburgers.nomoreparties.site/account/profile"  # url личный кабинет
    page_personal_account_label_here_you_can = By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"  # text - В этом разделе вы можете
    page_personal_account_logout_button_xpath = By.XPATH, ".//button[text()='Выход']"  # кнопка Выход
