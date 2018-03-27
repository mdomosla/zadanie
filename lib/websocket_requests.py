from websocket import create_connection


class Connection:

    @staticmethod
    def ask_for_hash(address, message):
        ws = create_connection(address)
        ws.send(message)
        result = ws.recv()
        return result
