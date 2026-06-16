# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    # Находим поле "Email" и заполняем его
    # Устанавливаем фокус на поле Email
    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for char in "qatest@gmail.com":
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.type(char, delay=300)

    # Выделяем весь текст в поле Email с помощью комбинации клавиш Ctrl+A
    page.keyboard.press("ControlOrMeta+A")
    page.wait_for_timeout(5000)
