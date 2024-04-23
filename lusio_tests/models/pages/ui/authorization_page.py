from selene import browser, have
import allure


class AuthorizationPage:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')
            browser.element(".personal-user__name").click()

    def filling_form(self, login, password):
        with allure.step('Заполнение формы авторизации'):
            browser.element('[name="USER_LOGIN"]').type(login)
            browser.element('[name="USER_PASSWORD"]').type(password)
            browser.element('[name="Login"]').click()

    def should_be_authorization_page(self):
        with allure.step('Проверка отображения страницы авторизации'):
            browser.element('.success_auth_form a[href="/personal/"]').should(
                have.exact_text("Ваш личный кабинет"))


authorization_page = AuthorizationPage()
