import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from config import BASE_DIR
from script.test_emp_hr import TestEmpHr
from script.test_login_hr import TestLoginHr
from utils import SessionUtils

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLoginHr))
suite.addTest(unittest.makeSuite(TestEmpHr))

# filename = BASE_DIR + "/report/tpshop{}.html".format(time.strftime("%H%m%d%H%M%S"))
filename = BASE_DIR + "/report/ihrm.html"
with open(filename, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2,title="报告标题", description="报告描述")
    runner.run(suite)

# 主动关闭
SessionUtils.quit_session()
