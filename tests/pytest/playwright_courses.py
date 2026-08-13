# Импорт Playwright для синхронного режима и проверок
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Открываем страницу регистрации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    # Заполняем форму регистрации
    # Поле "Email"
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    # Поле "Username"
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    # Поле "Password"
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    # Нажимаем кнопку "Registration"
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    #Сохраняем состояние браузера (storage state) в файл
    context.storage_state(path="browser-state.json")

    #Создаём новую сессию браузера с подстановкой сохранённого состояния
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    #Открываем страницу "Courses" — должна открыться без авторизации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    #Проверяем наличие и текст заголовка "Courses"
    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")
    
    #Проверяем иконку
    empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_view_icon).to_be_visible()

   
    #Проверяем наличие текста "There is no results"
    empty_view_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text("There is no results")

    #Проверяем наличие и текст описания блока
    empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
