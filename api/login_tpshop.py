from base.base_api import BaseApi
from config import VERIFY_URL_SHOP, LOGIN_URL_SHOP


class LoginApiTpShop(BaseApi):
    def __init__(self):
        super().__init__()

    def get_verify(self):
        return self.session.get(VERIFY_URL_SHOP)

    def get_login(self,username,password,verify_code):
        return self.session.post(LOGIN_URL_SHOP,
                      data={"username": username,
                            "password": password,
                            "verify_code": verify_code})
