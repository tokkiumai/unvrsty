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
    mb = []
    rest = ""
    r = a
    while True:
        m, r = gf2_core(r, b)
        mb.append(m)
        if m == "1" or m == "0":
            rest = r
            break
        if r == "0":
            break
    multiplier = mb[0]
    if len(mb) > 1:
        for i in range(1, len(mb)):
            multiplier = gf2_add(multiplier, mb[i])
    return multiplier, rest


def gf2_gcd(a: int, b: int) -> int:
    a1 = a
    b1 = b
    result = math.nan
    while True:
        _, r = gf2_core(a1, b1)
        if r == "0":
            break
        result = r
        a1 = b1
        b1 = r
    return result


def is_reducible(p: str) -> bool:
    d = int("0b" + p, 2)
    for i in range(2, d):
        if gf2_div(p, bin(i)[2:])[1] == "0":
            return False
    return True


def is_primitive(p: str) -> bool:
    pow = len(p) - 1
    m = 2 ** pow - 1
    l = generate_polynomial(pow, m)
    if gf2_div(l[len(l) - 1], p)[1] == "0":
        for i in range(0, len(l) - 1):
            d, m = gf2_div(l[i], p)
            if m == "0":
                return False
        return True
    return False


def generate_polynomial(n: int, m: int) -> list[str]:
    l = list()
    for p in range(n, m):
        new = "1" + "".join(["0" for _ in range(p)]) + "1"
        l.append(new)
    return l


def get_primitive_roots(p: list[str], field: int) -> list[str]:
    d = int("0b" + p, 2)
    first_root = None
    mod_l = None
    for i in range(2, d):
        x = i
        mod_l = [bin(x)[2:]]
        for j in range(2, field):
            x *= i
            mod = gf2_div(bin(x)[2:], p)[1]
            mod_l.append(mod)
            if mod == "1":
                if j != field - 1:
                    break
                else:
                    first_root = i
        if first_root:
            break
    result = list()
    for j in range(0, field - 1):
        if gf2_gcd(j + 1, field - 1) == 1:
            result.append(mod_l[j])
    return result
