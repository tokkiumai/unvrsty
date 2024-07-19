def format_and_encode(s):
    return " ".join(format(ord(x), 'b') for x in s).encode("utf-8")
