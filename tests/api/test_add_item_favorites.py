from lusio_tests.models.pages.api.item_favorites_page import item_favorites
import allure
from allure_commons.types import Severity
from lusio_tests.utils.api_helper import api_request


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('add discount card (api)')
@allure.story('add discount card from using api ')
@allure.link('https://lusio.ru', name='Testing')
def test_add_item_favorites(get_cookies):
    item_favorites.add(get_cookies, 127762)

    response = api_request('/personal/wishlist/', 'GET', cookies=get_cookies)

    item_favorites.should_add_item_be_favorites(response)

    item_favorites.delete(get_cookies, 127762)
