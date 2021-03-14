import unittest
from model.testutil import *
from model.functions import *
from Website.pageObject.LoginPage import LoginPage
from time import sleep


class TestLogin(SetStartAndEnd):

    def test_login1_normal(self):
        """输入正确的用户名和密码"""
        login = LoginPage(self.driver)
        login.login_action("51zxw", "123456")
        sleep(3)

        self.assertEqual("我的空间", login.check_login_pass())
        insert_img(self.driver, "login1_pass.png")

    def test_login2_pwd_error(self):
        """输入错误的用户密码"""
        login = LoginPage(self.driver)
        login.login_action("51zxw", "1234567")
        sleep(3)

        self.assertEqual("", login.check_login_fail())
        insert_img(self.driver, "login2_fail.png")

    def test_login3_pwd_and_username_blank(self):
        """输入空的用户名和密码"""
        login = LoginPage(self.driver)
        login.login_action("", "")
        sleep(3)

        self.assertEqual("", login.check_login_fail())
        insert_img(self.driver, "login3_fail.png")


if __name__ == '__main__':
    unittest.main()
