from utils import SessionUtils


class BaseApi:
    def __init__(self):
        self.session = SessionUtils.get_session()