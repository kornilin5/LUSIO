import allure
from config import settings
import requests


class AuthorizationPage:

    def authorization(self, cookies, endpoint):
        with allure.step('Авторизация пользователя'):
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}
            url = settings.domain_url + endpoint
            requests.post(url, cookies=cookies_dict)

    def should_access(self, response):
        with allure.step('проверка авторизации'):
            assert response.status_code == 200
            assert f'Здравствуйте, {settings.user_email} {settings.user_last_name}' in response.text


authorization_user = AuthorizationPage()
