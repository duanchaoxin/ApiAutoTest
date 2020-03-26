# 导包
import json
import unittest
from parameterized import parameterized
from api.login_hr import LoginHrApi
from utils import case_session_quit, LogUtil, assert_utils, getListData


class TestLoginHr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginHrApi()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        case_session_quit()

    @parameterized.expand(getListData("/data/test_login_hr.json"))
    def test01_login_success(self, case_name, json_data, status_code, success, code, message):
        response = self.login_api.get_login_hr(json_data=json_data)
        LogUtil.get_logger().info("登录成功的结果为：{}".format(response.json()))
        assert_utils(self, response, status_code, success, code, message)
