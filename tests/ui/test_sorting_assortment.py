from lusio_tests.models.pages.ui.sorting_assortment_page import sorting_assortment
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('sorting assortment')
@allure.story('sorting assortment from catalog')
@allure.link('https://lusio.ru', name='Testing')
def test_sorting_assortment():
    sorting_assortment.open()

    sorting_assortment.sort()

    sorting_assortment.should_be_sorting_assortment_page()
