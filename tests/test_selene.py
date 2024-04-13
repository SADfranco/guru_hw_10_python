from selene import browser, by, be


def test_issue_tab():
    browser.open('https://github.com/')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('SADfranco/ISTQBCertificate').press_enter()

    browser.element(by.link_text('SADfranco/ISTQBCertificate')).click()

    browser.element('#issues-tab').click()

    browser.element('#issue_2').should(be.visible)

