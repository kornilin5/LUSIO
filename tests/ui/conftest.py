from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from lusio_tests.utils import allure_attach


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="122.0")
    parser.addoption("--browser_name", default="chrome")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    from config import settings
    browser.config.base_url = settings.domain_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10.0
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else settings.default_version_browser
    browser_name = request.config.getoption('--browser_name')
    browser_name = browser_name if browser_name != "" else settings.default_verion_name_browser

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications-prompt")
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=settings.selenoid_url_authorization, options=options)

    browser.config.driver = driver
    yield

    allure_attach.add_screenshot(browser)
    allure_attach.add_logs(browser)
    allure_attach.add_html(browser)
    allure_attach.add_video(browser)

    browser.quit()
