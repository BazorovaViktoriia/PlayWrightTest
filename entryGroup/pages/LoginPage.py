class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_login_page(self, url):
        self.page.goto(url)

    def click_login_button(self):
        self.page.get_by_role("button", name="").click()

    def fill_email(self, email):
        self.page.locator("input[type=\"text\"]").fill(email)

    def fill_password(self, password):
        self.page.locator("input[type=\"password\"]").fill(password)

    def submit_login_form(self):
        self.page.get_by_role("button", name="Войти в систему").click()

    def submit_filial_form(self):
        self.page.get_by_role("button", name="").click()
