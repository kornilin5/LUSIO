from lusio_tests.models.pages.api.item_cart_page import item_cart
import allure
from allure_commons.types import Severity
from lusio_tests.utils.api_helper import api_request
from tests.api.conftest import get_cookies


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('add item cart (api+ui)')
@allure.story('adding a product using api + ui from the catalog to the cart')
@allure.link('https://lusio.ru', name='Testing')
def test_add_item_to_cart(get_cookies):
    form_data = {
        'action':
        'ADD2BASKET',
        'id':
        '127762',
        'ajax_basket':
        'Y',
        'quantity':
        1,
        'basket_props':
        'YToyOntpOjA7czo5OiJDT0xPUl9SRUYiO2k6MTtzOjEzOiJTSVpFU19DTE9USEVTIjt9'
    }
    item_cart.open()
    item_cart.authorization(get_cookies)
    item_cart.add_item(get_cookies,
                       '/catalog/odezhda/trikotazh_vyazanyy/',
                       data=form_data)

    response = api_request('/auth/', 'GET', cookies=get_cookies)

    item_cart.should_item_be_cart(response)

    item_cart.clear_cart()
