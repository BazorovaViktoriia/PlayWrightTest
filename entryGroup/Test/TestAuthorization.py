import configparser
from playwright.sync_api import Playwright, sync_playwright

from entryGroup.pages.LoginPage import LoginPage

class AccountPage:
    def __init__(self, page):
        self.page = page

    def click_logout_button(self):
        self.page.get_by_role("button", name="").click()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    config = configparser.ConfigParser()
    config.read("settings.ini")

    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.navigate_to_login_page(config.get('Settings', 'url'))
    login_page.click_login_button()
    login_page.fill_email(config.get('Settings', 'e_mail'))
    login_page.fill_password(config.get('Settings', 'password'))
    login_page.submit_login_form()
    login_page.submit_filial_form()

    page.wait_for_url(config.get('Settings', 'url_myAccount'))
    print(page.url)
    assert page.url == config.get('Settings', 'url_myAccount'), (f"Текущий URL (page.url) не "
                                                                 f"соответствует ожидаемому ({config.get('Settings', 'url_myAccount')})")

    account_page.click_logout_button()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
