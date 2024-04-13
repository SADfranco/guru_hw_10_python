import json
import allure
from allure import attachment_type
from selene.support.shared import browser

def test_attachments():
    allure.attach("It's text", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello Akhil Nadar</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"name": "Akhil", "surname": "Nadar", "email": "nadar@test.in"}), name="Json", attachment_type=attachment_type.JSON)
    allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=attachment_type.PNG)