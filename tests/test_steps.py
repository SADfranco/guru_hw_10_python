import allure
from selene import browser, by, be


def test_dynamic_steps():
    with allure.step("Открываем страницу GitHub"):
        browser.open('https://github.com/')

    with allure.step("Ищем нужный репозиторий"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('SADfranco/ISTQBCertificate').press_enter()

    with allure.step("Открываем репозиторий"):
        browser.element(by.link_text('SADfranco/ISTQBCertificate')).click()

    with allure.step("Переходим на вкладку ISUUES"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие ISSUES #2"):
        browser.element('#issue_2').should(be.visible)


def test_decorator_steps():
    open_main_page('https://github.com/')
    search_for_repo('SADfranco/ISTQBCertificate')
    open_repo('SADfranco/ISTQBCertificate')
    go_to_issues_tab()
    should_issues_visible_by_number(2)


@allure.step("Открываем страницу GitHub")
def open_main_page(link):
    browser.open(link)


@allure.step("Ищем нужный репозиторий")
def search_for_repo(name):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(name).press_enter()


@allure.step("Открываем репозиторий")
def open_repo(name):
    browser.element(by.link_text(name)).click()


@allure.step("Переходим на вкладку ISUUES")
def go_to_issues_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем наличие ISSUES #2")
def should_issues_visible_by_number(number):
    browser.element(f'#issue_{number}').should(be.visible)
