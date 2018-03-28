from tests.baseTest import *
from lib.websocket_requests import WebsocketRequests
from grappa import should
import time
from lib.random_generator import RandomGenerator


class WebSocketTest(BaseTest):
    ws_requests = WebsocketRequests()
    rg = RandomGenerator()

    def test_01_ask_for_hash_empty_message(self):
        response = self.ws_requests.ask_for_hash(address=self.CONFIG["WEBSOCKET_ADDRESS"], message='')
        response | should.not_be.none
        response | should.be.a('string')
        len(response) | should.be.higher.than(1)
        len(response) | should.be.lower.than(501)

    def test_02_ask_for_hash_random_string(self):
        message = self.rg.generate_random_string(10)
        response = self.ws_requests.ask_for_hash(address=self.CONFIG["WEBSOCKET_ADDRESS"], message=message)
        response | should.not_be.none
        response | should.be.a('string')
        len(response) | should.be.higher.than(1)
        len(response) | should.be.lower.than(501)

    def test_03_ask_for_hash_random_number(self):
        message = self.rg.get_date()
        response = self.ws_requests.ask_for_hash(address=self.CONFIG["WEBSOCKET_ADDRESS"], message=message)
        response | should.not_be.none
        response | should.be.a('string')
        len(response) | should.be.higher.than(1)
        len(response) | should.be.lower.than(501)