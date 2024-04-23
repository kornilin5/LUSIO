from selene import browser, be, have
import allure


class RegistrationPage:

    def open(self):
        with allure.step('Открытие страницы'):
            browser.open('/')
            browser.element('.personal-user__name').click()
            browser.element('.wrap_reg__link').click()

    def filling_form(self, **kwargs):
        with allure.step('Заполнение формы регистрации'):
            browser.element('[name="user_reg_email"]').type(kwargs['email'])
            browser.element('.auth-reg__step-email_submit').click()
            browser.element('[name="REGISTER[PASSWORD]"]').should(
                be.visible).type(kwargs['password'])
            browser.element('[name="REGISTER[CONFIRM_PASSWORD]"]').type(
                kwargs['confirm_password'])
            browser.element('[name="REGISTER[LAST_NAME]"]').type(
                kwargs['last_name'])
            browser.element('[name="REGISTER[NAME]"]').type(kwargs['name'])
            browser.element('[name="REGISTER[SECOND_NAME]"]').type(
                kwargs['second_name'])
            browser.element('[for="REGISTER[USER_AGREE]"]').click()
            browser.element('[name="register_submit_button"]').click()

    def should_be_registration_page(self):
        with allure.step('Проверка регистрации пользователя'):
            browser.all('.page__header').element_by(
                have.exact_text('Добро пожаловать'))


registration_page = RegistrationPage()
