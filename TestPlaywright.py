import configparser

from playwright.sync_api import Playwright, sync_playwright

config = configparser.ConfigParser()
config.read("settings.ini")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(config.get('Settings', 'url'))
    page.get_by_role("button", name="").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill(config.get('Settings', 'e_mail'))
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill(config.get('Settings', 'password'))
    page.get_by_role("button", name="Войти в систему").click()
    page.get_by_role("button", name="").click()
    page.wait_for_url(config.get('Settings', 'url_myAccount'))
    print(page.url)
    assert page.url == config.get('Settings', 'url_myAccount'), (f"Текущий URL (page.url) не "
                                                                 f"соответствует ожидаемому ({config.get('Settings', 'url_myAccount')})")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import configparser
from playwright.sync_api import Playwright, sync_playwright