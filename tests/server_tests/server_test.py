from tests.baseTest import *
from lib.server_requests import Requests
from grappa import should
import time


class ServerTest(BaseTest):
    server_requests = Requests()

    def test_01_check_server_response_for_all_users(self):
        users = self.file
        for user in users:
            result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=user)
            result['code'] | should.be.equal.to(200)
            result['response'] | should.be.a('string')
            result['response'] | should.not_be.equal.to(user)

    def test_02_check_server_response_for_no_user(self):
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"])
        result['code'] | should.not_be.equal.to(200)
        result['response'] | should.be.none

    def test_03_check_server_response_for_not_acceptable_data(self):
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=123)
        result['code'] | should.not_be.equal.to(200)
        result['response'] | should.be.none

    def test_04_check_hash_storing_on_server(self):
        users = self.file
        first_user = users[0]
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=first_user)
        hash_response = result['response']
        time.sleep(1)
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=first_user)
        second_hash = result['response']
        hash_response | should.be.equal.to(second_hash)

    def test_05_check_hash_asking_after_1_hour(self):
        users = self.file
        first_user = users[0]
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=first_user)
        hash_response = result['response']
        time.sleep(3601)
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=first_user)
        second_hash = result['response']
        hash_response | should.not_be.equal.to(second_hash)

    def test_06_check_server_response_for_unknown_user(self):
        users = self.file
        new_user = None
        for user in users:
            new_user += user
            # adding all user names will cause user that is 100% not present on list
        result = self.server_requests.post(self.CONFIG["SERVER_ADDRESS"], user=new_user)
        result['code'] | should.be.equal.to(200)
        result['response'] | should.be.none
