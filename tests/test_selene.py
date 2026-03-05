import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import be


def test_selene():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Наличие раздела Issue")
    allure.dynamic.link("https://github.com", name="Testing")

    browser.open("https://github.com")

    browser.element('//button[@data-target="qbsearch-input.inputButton"]').click()
    browser.element('//input[@id="query-builder-test"]').type('olegovnatim-lgtm/guru_hw_9').press_enter()
    browser.element('//a[@href="/olegovnatim-lgtm/guru_hw_9"]').click()
    browser.element('//span[@data-content="Issues"]').should(be.visible)
