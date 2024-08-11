import hashlib

from .util import format_and_encode, caesar_cipher


def hash_caesar_cipher(s, l):
    s_len = len(s)
    for _ in range(l):
        c = caesar_cipher(s, 4)
        s = format_and_encode(c)
        s = hashlib.md5(s).hexdigest()
    return s[:s_len]
