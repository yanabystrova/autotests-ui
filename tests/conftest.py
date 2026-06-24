import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

       
@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
         # print("Before")
        yield browser.new_page() #поток управления внутренним тестом
        # print("After")
        browser.close()