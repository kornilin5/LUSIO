from selene import browser, have, be
import allure


class AddItemCart:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')

    def add(self):
        with allure.step('Добавление товара в избранное'):
            browser.all('.menu__list .menu__item>a').element_by(
                have.text('Трикотаж')).click()
            browser.element('.catalog-page-bottom__btn').click()
            browser.element('[data-product-id="127738"]').hover().click()
            browser.element('.page-product__btns .page-product__btn').click()

    def should_item_be_cart(self):
        with allure.step('Проверка добавления в корзину'):
            browser.element('.btn-black[href="/personal/cart/"]').should(
                be.visible).click()
            browser.element('.basket-checkout-block-total-title').should(
                have.text("Ваш заказ")).click()
            browser.element('.basket-coupon-block-total-middle__text').should(
                have.text("1 товар"))

    def clear_cart(self):
        with allure.step('Очистка корзины'):
            browser.driver.refresh()
            browser.element('.personal-cart').click()
            browser.element('.btn-black[href="/personal/cart/"]').should(
                be.visible).click()
            browser.element('.basket-item-block-actions').click()


add_item_cart = AddItemCart()
