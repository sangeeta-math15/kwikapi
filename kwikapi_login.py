import json

from kwikapi import API, MockRequest, BaseRequestHandler, Request, BaseRequest
from typing import List

details = []


class Register(object):
    """
    create Registration class
    """
    def reg(self, a: str, b: str) -> List[List[str]]:
        """
        function reg returns user details
        """
        details.append([a, b])
        return details


class Login(object):
    """
    create Login class
    """
    def login(self, a: str, b: str) -> list:
        """
       function login returns user login successful or not
        """
        for user in details:
            if str(user[0]) == a and user[1] == b:
                return "login successful"
        return "login unsuccessful"


api = API()
api.register(Register(), "v1")
req = MockRequest(url="/api/v1/reg?a=sangeeta&b=123456")
res = json.loads(BaseRequestHandler(api).handle_request(req).decode('utf-8'))

api.register(Login(), "v2")
req2 = MockRequest(url="/api/v2/login?a=sangeeta&b=1234")
res2 = json.loads(BaseRequestHandler(api).handle_request(req2).decode('utf-8'))

print(res)
print(res['result'])

print(res2)
print(res2['result'])
