from lusio_tests.models.pages.ui.filter_item_material_page import filter_material
import allure
from allure_commons.types import Severity


@allure.tag('lusio_tests')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Filter item')
@allure.story('Filter item from catalog be material')
@allure.link('https://lusio.ru', name='Testing')
def test_filter_item_material():
    filter_material.open_page()

    filter_material.filter_item()

    filter_material.should_be_filtered()
