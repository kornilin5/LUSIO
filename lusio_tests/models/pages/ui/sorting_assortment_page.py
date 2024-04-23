from selene import browser, have, be
import allure


class SortingAssortment:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')
            browser.element('a.menu__link').should(
                have.exact_text("Каталог")).click()

    def sort(self):
        with allure.step('Сортировка ассортимента по скидке'):
            browser.all('.filter-item__title ').element_by(
                have.text('По популярности')).click()
            browser.all('.radio__text').element_by(
                have.text('Сначала со скидкой')).click()

    def should_be_sorting_assortment_page(self):
        with allure.step('Проверка отображения сортировки по скидке'):
            browser.all('.filter-item__title').element_by(
                have.text('Сначала со скидкой')).should(be.visible)


sorting_assortment = SortingAssortment()
