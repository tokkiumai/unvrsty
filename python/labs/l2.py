import math


def gf2_core(a: str, b: str) -> (str, str):
    if a == b:
        return "1", "0"
    da = len(a) - 1
    db = len(b) - 1
    if da < db:
        return "0", a
    if da == db:
        return "1", gf2_core(a, b)
    dm = da - db
    m = ["0" for _ in range(0, dm + 1)]
    m[0] = "1"
    m = "".join(m)
    ml = gf2_core(b, m)
    r = gf2_core(a, ml)
    return m, r


def gf2_add(a: str, b: str) -> str:
    rl = max(len(a), len(b))
    oa = "".join(["0" for _ in range(0, rl - len(a))])
    ob = "".join(["0" for _ in range(0, rl - len(b))])
    oa += a
    ob += b
    r = ""
    for i in range(rl):
        if oa[i] == "1" and ob[i] == "0" or oa[i] == "0" and ob[i] == "1":
            r += "1"
        else:
            r += "0"
    return r


def gf2_mul(a: str, b: str) -> str:
    ll = len(a) + len(b) - 1
    ls = []
    for i in range(len(b) - 1, -1, -1):
        if b[i] == "1":
            l = [0 for _ in range(0, ll)]
            for j in range(len(a) - 1, -1, -1):
                l[i + j] = int(a[j])
            ls.append(l)
    r = ""
    for j in range(0, ll):
        uq = 0
        for i in range(0, len(ls)):
            if ls[i][j] == 1:
                uq += 1
        if uq % 2 != 0:
            r += "1"
        else:
            r += "0"
    return r


def gf2_div(a: str, b: str) -> (str, str):
