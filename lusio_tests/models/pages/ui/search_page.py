from selene import browser, have
import allure


class SearchPage:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')

    def search_item(self):
        with allure.step('Поиск товара'):
            browser.element('.personal-search').click()
            browser.element('.digi-search-form__input').type(
                "Джинсы").press_enter()
            browser.all('.digi-facet-category__text').element_by(
                have.text('Джинсы')).click()

    def should_be_search_page(self):
        with allure.step('Проверка отображения страницы поиска с товаром'):
            browser.element('.digi-title').should(have.exact_text("ДЖИНСЫ"))


search_page = SearchPage()
