from .base_page import BasePage
from .locators import BasketPageLocators


class BooksPage(BasePage):
    def go_to_buy_book(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        link.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET), "Button add to basket is not presented"

    def should_be_text_about_add_to_basket(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET), "Button add to basket is not presented"

    def product_name(self):
        return self.browser.find_element(*BasketPageLocators.NAME_OF_PRODUCT).text

    def product_price(self):
        return self.browser.find_element(*BasketPageLocators.PRICE_OF_PRODUCT).text

    def should_be_all_text_about_add_to_basket(self):
        self.text_add_to_basket(self.product_name())
        self.text_about_price(self.product_price())

    def text_add_to_basket(self, name):
        assert self.is_element_present(*BasketPageLocators.TEXT_ADD_TO_BASKET_BOOK), "Adding message isn't presented"
        text_add_to_basket = self.browser.find_element(*BasketPageLocators.TEXT_ADD_TO_BASKET_BOOK).text
        assert text_add_to_basket == f"{name} has been added to your basket.", \
            "Text about add book incorrect"

    def text_about_price(self, price):
        assert self.is_element_present(*BasketPageLocators.TEXT_ADD_TO_BASKET_PRICE), "Price message isn't presented"
        text_price_basket = self.browser.find_element(*BasketPageLocators.TEXT_ADD_TO_BASKET_PRICE).text
        assert text_price_basket == f"Your basket total is now {price}", \
            "Text about price book incorrect"
