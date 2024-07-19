import string
import random


def generate_str(str_len, chars=string.ascii_lowercase):
    s = ''
    for _ in range(0, str_len):
        s += random.choice(chars)
    return s
