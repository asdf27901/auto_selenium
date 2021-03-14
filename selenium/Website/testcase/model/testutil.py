import unittest
from driver.driver import *
from Website.config.data_config import *


class SetStartAndEnd(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(timeout)

    def tearDown(self) -> None:
        self.driver.quit()
