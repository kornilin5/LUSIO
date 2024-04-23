import allure
from allure_commons.types import Severity
from lusio_tests.models.pages.ui.add_item_cart_page import add_item_cart


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('add item cart')
@allure.story('add item from catalog to cart')
@allure.link('https://lusio.ru', name='Testing')
def test_add_item_cart():
    add_item_cart.open()

    add_item_cart.add()

    add_item_cart.should_item_be_cart()
