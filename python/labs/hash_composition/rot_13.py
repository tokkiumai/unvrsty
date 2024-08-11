import hashlib
import codecs

from .util import format_and_encode


def hash_rot_13(s, l):
    s_len = len(s)
    for _ in range(l):
        t = codecs.encode(s, 'rot_13')
        s = format_and_encode(t)
        s = hashlib.md5(s).hexdigest()
    return s[:s_len]
