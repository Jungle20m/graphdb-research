import json


SIGNUP_NEW_ACCOUNT_API = "signupNewAccount"

class ApiObject:
    def __init__(self, date_=None, time_=None, ip=None, response_time=None, api_name="", error_status=None, json_log=None, log_location=None):
        self.date_ = date_
        self.time_ = time_
        self.ip = ip
        self.response_time = response_time
        self.api_name = api_name
        self.error_status = error_status
        self.json_log = json_log
        self.log_location = log_location

    @classmethod
    def get_from_row_of_log(cls, row):
        try:
            date_, time_, ip, response_time, api_name, error_status, json_log, log_location = row.split(" ")
            return cls(date_, time_, ip, response_time, api_name, error_status, json_log, log_location)
        except Exception as e:
            return cls()

    def is_signup_new_account(self):
        if self.api_name.startswith(SIGNUP_NEW_ACCOUNT_API):
            return True
        return False


class ApiSignupObject:
    def __init__(self, account_name="", device_key=""):
        self.account_name = account_name
        self.device_key = device_key

    @classmethod
    def get_from_api_json_log(cls, api_json_log):
        try:
            json_log = json.loads(api_json_log)
            return cls(account_name=json_log["account_name"], device_key=json_log["device_key"])
        except Exception as e:
            return cls()