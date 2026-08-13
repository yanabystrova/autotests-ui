import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()  # поток управления внутренним тестом
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Регистрируем нового пользователя и сохраняем состояние браузера.
    # Выполняется один раз за всю сессию тестирования.
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    registration_page = RegistrationPage(page=page)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
    registration_page.click_registration_button()

    # Сохраняем состояние браузера (storage state) в файл
    context.storage_state(path="browser-state.json")

    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    # Открываем новую страницу, используя сохранённое состояние из browser-state.json
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
