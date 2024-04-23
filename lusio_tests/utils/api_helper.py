import requests
from lusio_tests.utils.allure_attach import response_logging, response_attaching


def api_request(endpoint, method, cookies, **kwargs):
    from config import settings
    url = f"{settings.domain_url}{endpoint}"
    cookies_dict = {cookie.name: cookie.value for cookie in cookies}
    response = requests.request(method, url, cookies=cookies_dict, **kwargs)
    response_logging(response)
    response_attaching(response)
    return response
