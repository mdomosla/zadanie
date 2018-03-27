import requests


class Requests:

    def post(self, address, **payload):
        r = requests.post(address, payload)
        resp = {"response": r.json(), "code": r.status_code}
        return resp
