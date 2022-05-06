from django.utils.crypto import get_random_string


def generate_random_string(length):
    code = get_random_string(length=length)
    return code.upper()