# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("testingqa@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("qatester")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("123456@")

    # Находим кнопку "Login" и кликаем на нее
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Проверяем, что после регистрации произошёл переход на страницу Dashboard
    # Проверяем, что URL содержит "/dashboard"
    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # Проверяем, что заголовок "Dashboard" виден на странице
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
