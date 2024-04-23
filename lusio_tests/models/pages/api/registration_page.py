import requests
from config import settings
import allure
from lusio_tests.utils.api_helper import api_request

class RegistrationPage:
    response = None
    
    def registration(self, data, params):
        with allure.step('Регистрация пользователя'):
            self.response = requests.post(url=settings.domain_url + '/auth/',
                                    params=params,
                                    data=data,
                                    allow_redirects=False)
            assert self.response.status_code == 200
            
    def should_access(self, data):
        with allure.step('проверка с помощью авторизации'):
            response = api_request(
            endpoint='/auth/',
            method='POST',
            cookies=self.response.cookies,
            data=data,
            
        )
            assert response.status_code == 200
            assert (f'Здравствуйте, {data['USER_NAME']} {data['USER_LAST_NAME']}' in response.text)


registration_user = RegistrationPage()
