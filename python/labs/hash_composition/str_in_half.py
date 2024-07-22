import hashlib
from util import format_and_encode


def hash_str_in_half(s, loops):
    str_len = len(s)
    for _ in range(loops):
        s = format_and_encode(s)
        p1 = s[0:str_len // 2]
        p2 = s[str_len // 2 if str_len % 2 == 0 else ((str_len // 2) + 1):]
        s = hashlib.md5(p1).hexdigest() + hashlib.md5(p2).hexdigest()
    return s[:str_len]
