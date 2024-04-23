from lusio_tests.data.users import user
from lusio_tests.models.pages.ui.registration_page import registration_page
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('registration page')
@allure.story('registration page with random faker login and password')
@allure.link('https://lusio.ru', name='Testing')
def test_registration_page():
    registration_page.open()

    registration_page.filling_form(
        email=user.create_email(),
        password=user.create_password(),
        confirm_password=user.create_confirm_password(),
        last_name=user.create_last_name(),
        name=user.create_name(),
        second_name=user.create_second_name(),
    )

    registration_page.should_be_registration_page()
