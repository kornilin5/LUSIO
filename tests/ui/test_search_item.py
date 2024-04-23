from lusio_tests.models.pages.ui.search_page import search_page
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('search item')
@allure.story('search item from catalog')
@allure.link('https://lusio.ru', name='Testing')
def test_search_item():
    search_page.open()

    search_page.search_item()

    search_page.should_be_search_page()
