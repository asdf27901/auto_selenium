from selenium import webdriver


def get_driver():

    # 返回谷歌浏览器对象
    driver = webdriver.Chrome()
    # 返回火狐浏览器对象
    # driver = webdriver.Firefox()
    # 返回IE浏览器对象
    # driver = webdriver.Ie()

    # driver.get("http://www.baidu.com")
    return driver


if __name__ == '__main__':
    get_driver()
