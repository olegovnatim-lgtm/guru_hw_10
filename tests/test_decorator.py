import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import be

# Второй способ
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "timofeevaao")
@allure.feature("Задачи в репозитории")
@allure.story("Наличие раздела Issue")
@allure.link("https://github.com", name="Testing")
def test_selene():
    open_main_page()
    search_repository()
    open_repository_from_search()
    find_issues()


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Ввести в поле поиска наименование искомого репозитория и нажать Enter")
def search_repository():
    browser.element('//button[@data-target="qbsearch-input.inputButton"]').click()
    browser.element('//input[@id="query-builder-test"]').type('olegovnatim-lgtm/guru_hw_9').press_enter()

@allure.step("Перейти в репозиторий из результатов поиска")
def open_repository_from_search():
    browser.element('//a[@href="/olegovnatim-lgtm/guru_hw_9"]').click()

@allure.step("Проверить наличие раздела 'Issues'")
def find_issues():
    browser.element('//span[@data-content="Issues"]').should(be.visible)
