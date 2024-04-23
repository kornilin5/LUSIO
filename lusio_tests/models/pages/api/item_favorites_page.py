import requests
from config import settings
import allure


class ItemFavorites:

    def add(self, cookies, id):
        with allure.step('Добавление товара в избранное'):
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}
            response = requests.get(
                f"{settings.domain_url}/local/ajax/favorites.php?id={id}",
                cookies=cookies_dict,
            )
            assert response.status_code == 200

    def should_add_item_be_favorites(self, response):
        with allure.step('Проверка добавления в избранное'):
            assert response.status_code == 200
            assert '127762' in response.text

    def delete(self, cookies, id):
        with allure.step('Удаление товара из избранного'):
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}
            response = requests.get(
                f"{settings.domain_url}/local/ajax/favorites.php?id={id}",
                cookies=cookies_dict,
            )
            assert response.status_code == 200

    def should_delete_item_from_favorites(self, response):
        with allure.step('проверка удаления из избранного'):
            assert response.status_code == 200
            assert 'Трикотажный топ в полоску' not in response.text
            assert '127762' not in response.text


item_favorites = ItemFavorites()
