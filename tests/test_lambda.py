import allure
from selene.support.conditions import be
from selene.support.shared import browser


def test_lambda():

    with allure.step("Открыть главную страницу"):
        browser.open("https://github.com")

    with allure.step("Кликнуть в поле поиска"):
        browser.element('//button[@data-target="qbsearch-input.inputButton"]').click()

    with allure.step("Ввести наименование искомого репозитория и нажать Enter"):
        browser.element('//input[@id="query-builder-test"]').type('olegovnatim-lgtm/guru_hw_9').press_enter()

    with allure.step("Перейти в репозиторий"):
        browser.element('//a[@href="/olegovnatim-lgtm/guru_hw_9"]').click()

    with allure.step("Проверить наличие раздела 'Issues'"):
        browser.element('//span[@data-content="Issues"]').should(be.visible)