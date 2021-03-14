import os
from driver.driver import *


def insert_img(driver, filename):
    path = os.path.dirname(__file__)
    base_path = os.path.dirname(path)
    base_path = str(base_path).replace("\\", "/")
    base_path = base_path.split("/testcase")[0]

    file_path = base_path + "/testreport/screenshot/" + filename
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = get_driver()
    driver.get("http://www.baidu.com")

    insert_img(driver, "1111.jpg")
