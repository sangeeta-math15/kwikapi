import json

from kwikapi import API, MockRequest, BaseRequestHandler


class Calc(object):
    # Type information must be specified
    def add(self, a: int, b: int) -> int:
        return a + b


api = API()
api.register(Calc(), "v1")  # `v1` is the version of this example

req = MockRequest(url="/api/v1/add?a=10&b=20")
res = json.loads(BaseRequestHandler(api).handle_request(req).decode('utf-8'))

print(res['result'])
