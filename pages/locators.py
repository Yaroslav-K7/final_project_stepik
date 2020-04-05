from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_BUTTON = (By.XPATH, "//*[@name='login_submit']")
    REGISTER_BUTTON = (By.XPATH, "//*[@name='registration_submit']")


class BasketPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//*[contains(@class, 'btn-add-to-basket')]")
    NAME_OF_PRODUCT = (By.XPATH, "(//*[contains(@class, 'product_main')])/h1")
    PRICE_OF_PRODUCT = (By.XPATH, "(//*[contains(@class, 'price_color')])[2]")
    SUCCESS_MESSAGE = (By.XPATH, "(//*[contains(@class, 'alertinner')])[1]")
    TEXT_ADD_TO_BASKET_PRICE = (By.XPATH, "(//*[contains(@class, 'alertinner')])[3]//p[1]")

