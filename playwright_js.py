from playwright.sync_api import sync_playwright

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle",  # Ждем полной загрузки страницы
    )
    # Выполняем JS-код для замены текста заголовка
    new_text = "New Text"
    page.evaluate(
        """
        (text) => {
             const title = document.getElementById('authentication-ui-course-title-text')
             title.textContent = text
        }
        """,
        new_text, # Передаём аргумент из Python
    )

    page.wait_for_timeout(5000)
