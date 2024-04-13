import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")

    browser.open('https://github.com/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('SADfranco/ISTQBCertificate').press_enter()
    browser.element(by.link_text('SADfranco/ISTQBCertificate')).click()
    browser.element('#issues-tab').click()
    browser.element('#issue_2').should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    browser.open('https://github.com/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('SADfranco/ISTQBCertificate').press_enter()
    browser.element(by.link_text('SADfranco/ISTQBCertificate')).click()
    browser.element('#issues-tab').click()
    browser.element('#issue_2').should(be.visible)