from selene import browser, have, be
import allure


class AddItemFavorites:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')
            browser.all('.menu__list .menu__item>a').element_by(
                have.text('Трикотаж')).click()

    def add(self):
        with allure.step('Добавление товара в избранное'):
            browser.element('.catalog-page-bottom__btn').click()
            browser.element(
                '[data-product-id="127738"] .product-card__favorite').click()

    def should_be_favorites_page(self):
        with allure.step('Проверка добавления в избранное'):
            browser.element('.personal-wishlist').click()
            browser.element(
                '.personal-dropdown [href="/personal/wishlist/"]').click()
            browser.element(".product-item-wishlist-card").should(be.visible)
            browser.element('.wishlist_count').should(have.text("1"))


add_item_favorites = AddItemFavorites()
