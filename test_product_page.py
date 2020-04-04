from .pages.product_page import BooksPage
import time


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = BooksPage(browser, link)
    page.open()
    page.go_to_buy_book()
    page.solve_quiz_and_get_code()
    page.should_be_all_text_about_add_to_basket()
