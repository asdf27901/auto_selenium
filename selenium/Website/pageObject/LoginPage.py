from selenium.webdriver.common.by import By
from Website.pageObject.BasePage import *


class LoginPage(Page):

    url = data_config.login_url
    username_loc = (By.NAME, "username")
    password_loc = (By.NAME, "password")
    submit_loc = (By.NAME, "Submit")
    login_pass = (By.LINK_TEXT, "我的空间")

    def type_username(self, username):
        self.find_element(*LoginPage.username_loc).clear()
        self.find_element(*LoginPage.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*LoginPage.password_loc).clear()
        self.find_element(*LoginPage.password_loc).send_keys(password)
        self.find_element(*LoginPage.submit_loc).click()

    def check_login_pass(self):
        return self.find_element(*LoginPage.login_pass).text

    def check_login_fail(self):
        return self.find_element(*LoginPage.password_loc).text

    def login_action(self, username, password):
        LoginPage(self.driver).open(LoginPage.url)

        self.type_username(username)
        self.type_password(password)
