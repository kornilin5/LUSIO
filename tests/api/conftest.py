import requests
import pytest


@pytest.fixture
def get_cookies():
    from config import settings
    data = {
        "bxajaxid": "2a4c24597c2115afc1fb50b26b3d69f9",
        "AJAX_CALL": "Y",
        "AUTH_FORM": "Y",
        "TYPE": "AUTH",
        "USER_LOGIN": settings.user,
        "USER_PASSWORD": settings.password,
    }
    response = requests.post(url=settings.domain_url + '/auth/',
                             params={'login': 'yes'},
                             data=data,
                             allow_redirects=False)
    cookies = response.cookies
    return cookies
