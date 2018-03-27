import os
import json


class ConfigReader:

    @staticmethod
    def load_configuration_from_file(file_name):
        with open(file_name, 'r') as file:
            config = json.load(file)
        return config
