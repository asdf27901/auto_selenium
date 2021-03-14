import unittest
import time
from BSTestRunner import BSTestRunner

testcase_path = "./Website/testcase/"
testreport_path = "./Website/testreport/"
report = unittest.defaultTestLoader.discover(testcase_path, "*test.py")

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    reportname = testreport_path + "/" + now + "result.html"
    with open(reportname, "wb") as f:
        BSTestRunner(stream=f, title="51自学网登录测试", description="测试详情").run(report)
    f.close()
