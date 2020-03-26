# 导包
import json
import unittest
from parameterized import parameterized
from api.login_tpshop import LoginApiTpShop
from config import BASE_DIR
from utils import case_session_quit, LogUtil


def getLoginData():
    data = []
    with open(BASE_DIR + "/data/test_login_tpshop.json", "r", encoding="utf-8") as f:
        python_data = json.load(f)
        LogUtil.get_logger().info(python_data)
        for d in python_data:
            username = d.get("username")
            password = d.get("password")
            verify_code = d.get("verify_code")
            status_code = d.get("status_code")
            status = d.get("status")
            msg = d.get("msg")
            data.append((username,password,verify_code,status_code,status,msg))
        # 3.返回参数化数据的结果列表
    return data


class TestLoginTpShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApiTpShop()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        case_session_quit()

    @parameterized.expand(getLoginData())
    def test01_login_success(self,username,password,verify_code,status_code,status,msg):
        response_verify = self.login_api.get_verify()
        self.assertEqual("image/png", response_verify.headers.get("Content-Type"))

        response_login = self.login_api.get_login(username,password,verify_code)

        print("登陆的结果为：", response_login.json())

        self.assertEqual(status_code, response_login.status_code)
        self.assertEqual(status, response_login.json().get("status"))
        self.assertEqual(msg, response_login.json().get("msg"))

