import config
from base.base_api import BaseApi
from config import HEADERS, EMP_HR, EMP_ID


class EmpHrApi(BaseApi):
    def __init__(self):
        super().__init__()

    def add_emp_hr(self, json_data):
        return self.session.post(url=EMP_HR, json=json_data, headers=HEADERS)

    def select_emp_hr(self):
        return self.session.get(url=EMP_HR + "/" + config.EMP_ID, headers=HEADERS)

    def put_emp_hr(self, put_json):
        return self.session.put(url=EMP_HR + "/" + config.EMP_ID, json=put_json, headers=HEADERS)

    def delete_emp_hr(self):
        return self.session.delete(url=EMP_HR + "/" + config.EMP_ID, headers=HEADERS)
