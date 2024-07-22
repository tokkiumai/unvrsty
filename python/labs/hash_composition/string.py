import hashlib
from util import format_and_encode


def hash_str(s, loops):
    str_len = len(s)
    for _ in range(loops):
        s = format_and_encode(s)
        s = hashlib.md5(s).hexdigest()
    return s[:str_len]
