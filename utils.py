import json
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import requests
from config import BASE_DIR


class SessionUtils:
    session = None

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session

    @classmethod
    def quit_session(cls):
        if cls.session is not None:
            cls.session.close()


# 用例驱动退出方法
def case_session_quit():
    if BASE_DIR != os.getcwd():
        SessionUtils.quit_session()


# 用于封装日志器工具
class LogUtil:
    # 保存日志器
    logger = None

    # 获取日志器
    @classmethod
    def get_logger(cls):
        # 如果当前日志器是空, 无法返回
        # 先创建设置好日志器, 保存在logger属性中
        # 最后在返回
        if cls.logger is None:
            # 1.创建日志器 导入logging
            cls.logger = logging.getLogger("logger")
            cls.logger.setLevel(logging.INFO)

            # 2.获取处理器 -- 控制台处理 - 时间分割文件
            shl = logging.StreamHandler()
            trfl = TimedRotatingFileHandler(filename=BASE_DIR + "/log/log.log",  # 日志保存的位置要统一到项目log目录下
                                            when="midnight",
                                            interval=1,
                                            backupCount=0,
                                            encoding="utf-8"
                                            )
            # 3.获取格式器
            fmter = logging.Formatter(
                fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

            # 4.处理器设置格式器
            shl.setFormatter(fmter)
            trfl.setFormatter(fmter)

            # 5.日志器添加处理器
            cls.logger.addHandler(shl)
            cls.logger.addHandler(trfl)

        return cls.logger


def getListData(filepath):
    data = list()
    with open(BASE_DIR + filepath, "r", encoding="utf-8") as f:
        python_data = json.load(f)
        LogUtil.get_logger().info(python_data)
        for d in python_data:
            data.append(d.values())
    # 3.返回参数化数据的结果列表
    return data

def getDictData(filepath,key):
    data = list()
    with open(BASE_DIR + filepath, "r", encoding="utf-8") as f:
        python_data = json.load(f).get(key)
        LogUtil.get_logger().info(python_data)
        data.append(python_data.values())
    # 3.返回参数化数据的结果列表
    return data

def assert_utils(self, response, status_code, success, code, message):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))
