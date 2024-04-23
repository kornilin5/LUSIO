import requests
from config import settings
import allure
from selene import browser, be


class ItemCart:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')

    def authorization(self, cookies):
        with allure.step('Авторизация пользователя'):
            for cookie in cookies:
                browser.driver.add_cookie({
                    "name": cookie.name,
                    "value": cookie.value,
                    "path": cookie.path,
                    "domain": cookie.domain
                })

    def add_item(self, cookies, endpoint, **kwargs):
        with allure.step('Добавление в корзину'):
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}
            respons = requests.post(settings.domain_url + endpoint,
                                    cookies=cookies_dict,
                                    **kwargs)
            assert respons.status_code == 200

    def should_item_be_cart(self, response):
        with allure.step('Проверка добавления в корзину'):
            assert 'Трикотажный топ в полоску' in response.text, "Трикотажный топ в полоску не найден в тексте ответа"
            assert '127762' in response.text, "PRODUCT_ID 127762 не найден в тексте ответа"

    def clear_cart(self):
        with allure.step('Очистка корзины'):
            browser.driver.refresh()
            browser.element('.personal-cart').click()
            browser.element('.btn-black[href="/personal/cart/"]').should(
                be.visible).click()
            browser.element('.basket-item-block-actions').click()


item_cart = ItemCart()
