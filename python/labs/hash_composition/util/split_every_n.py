def split_every_n(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]
