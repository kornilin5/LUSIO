from lusio_tests.models.pages.api.item_favorites_page import item_favorites
import allure
from allure_commons.types import Severity
from lusio_tests.utils.api_helper import api_request


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('delete item favorites (api)')
@allure.story('delete item from using api catalog to favorites')
def test_delete_item_from_favorites(get_cookies):
    item_favorites.add(get_cookies, 127762)

    item_favorites.delete(get_cookies, 127762)

    response = api_request('/personal/wishlist/', 'GET', cookies=get_cookies)

    item_favorites.should_delete_item_from_favorites(response)
