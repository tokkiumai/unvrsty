import hashlib
from util import format_and_encode, split_every_n


def hash_str_by_four(s, loops):
    str_len = len(str)
    for _ in range(loops):
        sp = split_every_n(s, 4)
        new = ""
        for item in sp:
            i = format_and_encode(item)
            new += hashlib.md5(item).hexdigest()
        s = new
    return s[:str_len]
