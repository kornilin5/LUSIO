from lusio_tests.models.pages.ui.add_item_favorites_page import add_item_favorites
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('add item favorites')
@allure.story('add item from catalog to favorites')
@allure.link('https://lusio.ru', name='Testing')
def test_add_item_favorites():
    add_item_favorites.open()

    add_item_favorites.add()

    add_item_favorites.should_be_favorites_page()
