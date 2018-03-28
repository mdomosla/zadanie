import string
import random
from datetime import datetime


class RandomGenerator:

    @staticmethod
    def generate_random_string(length):
        generated_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return generated_string

    @staticmethod
    def get_date():
        current_date = datetime.now()
        data_formatted = str(current_date.strftime('%Y%m%d%H%M%S%f'))
        return data_formatted
