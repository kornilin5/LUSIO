from selene import browser, have
import allure


class FilterItemMaterial:

    def open_page(self):
        with allure.step('Открытие страницы'):
            browser.open('/')
            browser.element('a.menu__link').should(
                have.exact_text("Каталог")).click()

    def filter_item(self):
        with allure.step('фильтрация товара по материалу'):
            browser.all('.catalog-custom-menu__link').element_by(
                have.text('Трикотаж вязаный')).click()
            browser.all(".filter-item__title").element_by(
                have.text('Материал')).click()
            browser.all(".checkbox__text").element_by(
                have.text('вискоза')).click()
            browser.element(
                '.filter-item__active .filter-item__body-btn').click()

    def should_be_filtered(self):
        with allure.step('Проверка фильтрации'):
            browser.element('.product-card__title').should(
                have.exact_text("Лонгслив прямого кроя"))


filter_material = FilterItemMaterial()
