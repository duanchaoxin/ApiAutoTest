import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_HOST_TPSHOP = "http://localhost/"
BASE_HOST_HR = "http://182.92.81.159/"
HEADERS = {"Content-Type": "application/json"}
# tpshop验证码接口
VERIFY_URL_SHOP = BASE_HOST_TPSHOP + "index.php?m=Home&c=User&a=verify"
# tpshop登录接口
LOGIN_URL_SHOP = BASE_HOST_TPSHOP + "index.php?m=Home&c=User&a=do_login"
# hr登录接口
LOGIN_URL_HR = BASE_HOST_HR + "api/sys/login"
# hr员工接口
EMP_HR = BASE_HOST_HR + "api/sys/user"
EMP_ID = ""
