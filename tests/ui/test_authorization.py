from lusio_tests.models.pages.ui.authorization_page import authorization_page
from config import settings
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('authorization page')
@allure.story('authorization page with login and password')
@allure.link('https://lusio.ru', name='Testing')
def test_authorization_page():
    authorization_page.open()

    authorization_page.filling_form(settings.user, settings.password)

    authorization_page.should_be_authorization_page()
