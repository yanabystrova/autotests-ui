# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()
    
    context.storage_state(path='browser-state.json')
    
        # Проверяем, что после регистрации произошёл переход на страницу Dashboard
    # Проверяем, что URL содержит "/dashboard"
    # expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # # Проверяем, что заголовок "Dashboard" виден на странице
    # dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    # expect(dashboard_title).to_be_visible()
    # expect(dashboard_title).to_have_text("Dashboard")
    
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
     
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
   
    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
