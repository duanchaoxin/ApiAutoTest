from base.base_api import BaseApi
from config import LOGIN_URL_HR, HEADERS


class LoginHrApi(BaseApi):
    def __init__(self):
        super().__init__()

    def get_login_hr(self,json_data):
        return self.session.post(LOGIN_URL_HR,json=json_data,headers=HEADERS)
