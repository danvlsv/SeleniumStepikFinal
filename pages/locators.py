from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_INPUT_1 = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR,"[name='registration_submit']")

class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main h1')
    ADDED_NAME=(By.CSS_SELECTOR,"#messages .alert:first-of-type strong")

class BasketLocators():
    BASKET_BTN = (By.CSS_SELECTOR,"span.btn-group a")
    BASKET_FORM = (By.CSS_SELECTOR,"#basket_formset")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR,"div#content_inner > p")