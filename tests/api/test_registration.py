from lusio_tests.models.pages.api.registration_page import registration_user
from lusio_tests.data.users import user
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('registration (api)')
@allure.story('registration using api and faker login and password')
def test_registration():
    data = {
        'AUTH_FORM': 'Y',
        'TYPE': 'REGISTRATION',
        'USER_NAME': user.create_name(),
        'USER_LAST_NAME': user.create_last_name(),
        'USER_LOGIN': user.create_login(),
        'USER_PASSWORD': user.create_password(),
        'USER_CONFIRM_PASSWORD': user.create_confirm_password(),
        'USER_EMAIL': user.create_email()
    }
    params = {'register': 'yes'}

    registration_user.registration(data, params)

    registration_user.should_access(data)
