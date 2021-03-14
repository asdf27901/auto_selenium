from Website.config import data_config
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = data_config.base_url
        self.timeout = data_config.timeout

    def __open(self, append_url: str) -> None:
        url = self.base_url + append_url
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)
        sleep(3)
        assert self.driver.current_url == url, "不是当前的url："+url

    def open(self, url) -> None:
        self.__open(url)

    def find_element(self, *args):
        return self.driver.find_element(*args)
