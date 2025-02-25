from components.base import BaseComponent


class LoginForm(BaseComponent):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'

    def set_login(self, login):
        self.wait_until_and_get_elem_by_xpath(self.LOGIN).send_keys(login)

    def next(self):
        self.wait_until_and_get_elem_by_xpath(self.NEXT_BUTTON).click()

    def set_password(self, password):
        self.wait_until_and_get_elem_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.wait_until_and_get_elem_by_xpath(self.SUBMIT).click()
