from lusio_tests.models.pages.api.authorization_page import authorization_user
import allure
from allure_commons.types import Severity
from lusio_tests.utils.api_helper import api_request


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('authorization (api)')
@allure.story('authorization using api')
@allure.link('https://lusio.ru', name='Testing')
def test_authorization(get_cookies):
    authorization_user.authorization(get_cookies, '/auth/')

    response = api_request(
        '/auth/',
        'POST',
        get_cookies,
    )
    authorization_user.should_access(response)
