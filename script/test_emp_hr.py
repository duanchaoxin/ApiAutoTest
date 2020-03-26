# 导包
import unittest
from parameterized import parameterized
import config
from api.emp_hr import EmpHrApi
from api.login_hr import LoginHrApi
from utils import case_session_quit, LogUtil, assert_utils, getDictData


class TestEmpHr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginHrApi()
        cls.emp_api = EmpHrApi()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        case_session_quit()

    @parameterized.expand(getDictData("/data/test_emp_hr.json","login_data"))
    def test01_login_success(self, json_data, status_code, success, code, message):
        # 登录
        response = self.login_api.get_login_hr(json_data=json_data)
        LogUtil.get_logger().info("登录成功的结果为：{}".format(response.json()))
        assert_utils(self, response, status_code, success, code, message)
        headers = {"Authorization": "Bearer " + response.json().get("data")}
        config.HEADERS.update(headers)

    # @parameterized.expand(getDictData("/data/test_emp_hr.json", "login_data"))
    # def test02_emp_add(self, code, emp_json, message, response, status_code, success):
    #     # 添加员工
    #     response = self.emp_api.add_emp_hr(emp_json)
    #     # 打印添加的结果
    #     LogUtil.get_logger().info("添加员工的结果为：{}".format(response.json()))
    #     assert_utils(self, response, status_code, success, code, message)
    #     return response
    #
    # @parameterized.expand(getDictData("/data/test_emp_hr.json", "login_data"))
    # def test03_emp_select(self, code, message, response, status_code, success):
    #     # 查询员工
    #     config.EMP_ID = response.json().get("data").get("id")
    #     response = self.emp_api.select_emp_hr()
    #     LogUtil.get_logger().info("查询员工的结果为：{}".format(response.json()))
    #     assert_utils(self, response, status_code, success, code, message)
    #
    # @parameterized.expand(getDictData("/data/test_emp_hr.json", "login_data"))
    # def test04_emp_put(self, code, message, put_json, status_code, success):
    #     # 修改员工
    #     response = self.emp_api.put_emp_hr(put_json)
    #     LogUtil.get_logger().info("修改员工的结果为：{}".format(response.json()))
    #     import pymysql
    #     # 连接数据库
    #     conn = pymysql.connect(host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm')
    #     # 获取游标
    #     cursor = conn.cursor()
    #     # 执行查询的SQL语句
    #     sql = "select username from bs_user where id={}".format(config.EMP_ID)
    #     # 输出SQL语句
    #     LogUtil.get_logger().info("打印SQL语句：{}".format(sql))
    #     cursor.execute(sql)
    #     # 调试执行的SQL结果
    #     result = cursor.fetchone()
    #     LogUtil.get_logger().info("执行SQL语句查询的结果为：{}".format(result))
    #     # 关闭游标
    #     cursor.close()
    #     # 关闭连接
    #     conn.close()
    #     # 断言数据库查询的结果
    #     self.assertEqual("tom", result[0])
    #     assert_utils(self, response, status_code, success, code, message)
    #
    # @parameterized.expand(getDictData("/data/test_emp_hr.json", "login_data"))
    # def test05_emp_delete(self, code, message, status_code, success):
    #     # 删除员工
    #     response = self.emp_api.delete_emp_hr()
    #     LogUtil.get_logger().info("删除员工的结果为：{}".format(response.json()))
    #     assert_utils(self, response, status_code, success, code, message)


