import math
import random
import numpy as np


def gcd(x: float, y: float) -> int:
    return int(gcd_core(math.fabs(x), math.fabs(y)))


def gcd_core(x: float, y: float) -> float:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def gcd_extended(x: float, y: float) -> (float, int, int):
    if x == 0:
        return y, 0, 1
    gcd_result, x1, y1 = gcd_extended(y % x, x)
    return gcd_result, y1 - (y // x) * x1, x1


def euler(n: float) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result *= 1.0 - (1.0 / float(p))
        p = p + 1
    if n < 1:
        result *= 1.0 - (1.0 / float(n))
    return int(result)


def primes(start: int, end: int) -> list[int]:
    result = []
    for n in range(start, end):
        status = True
        for d in range(2, math.isqrt(n)):
            if n % d == 0:
                status = False
                break
        if status:
            result.append(n)
    return result


def generate_primes(start=2, end=2):
    primes_ns = primes(start, end)
    return primes_ns[random.randint(0, len(primes_ns) - 1)]


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def is_perfect_square(x: int) -> bool:
    return x == math.isqrt(x) ** 2


def solve_diophantine_eq(a: float, b: float, c: float) -> float:
    d = gcd(a, c)
    if b % d == 0:
        x, _ = solve_diophantine_eq(a, c, b)
        return x % c
    return math.nan


def solve_comparison_eq(a: int, b: int, c: int) -> (float, float):
    should_solve = c % gcd(a, b) == 0
    if should_solve:
        _, xg, yg = gcd_extended(a, b)
        return xg * c, yg * c
    return math.nan, math.nan


def solve_comparison_fermat_eq(a: float, b: float, c: float) -> str:
    d = gcd(a, c)
    if d == 1:
        x = str(((a ** (euler(c) - 1)) * b) % c)
    else:
        if b % d == 0:
            a1 = a // d
            b1 = b // d
            c1 = c // d
            x1 = ((a1 ** (euler(c1) - 1)) * b1) % c1
            x = str(c1) + "k+ " + str(x1) + "(mod " + str(c) + "), k ∈ {0,...," + str(d - 1) + "}"
        else:
            x = "no solutions"
    return x


def get_relative_primes(p: int, start=1, end=1) -> list[int]:
    result = []
    if end == 0:
        end = p
    for i in range(start, end):
        if gcd(i, p) == 1:
            result.append(i)
    return result


def generate_relative_primes(n: int) -> int:
    r = get_relative_primes(n, 2, 0)
    return r[random.randint(0, len(r) - 1)]


def get_primitive_roots(n: int) -> list[int]:
    for i in range(2, n):
        for j in range(1, n):
            value = (i ** j) % n
            if value == 1:
                if j == n - 1:
                    prime_nums = get_relative_primes(n - 1, 1, n - 1)
                    result = []
                    for rp in prime_nums:
                        result.append(int((i ** rp) % n))
                    return result
                else:
                    break
    return []


def generate_primitive_roots(n: int) -> int:
    roots = get_primitive_roots(n)
    return roots[random.randint(0, len(roots) - 1)]


def chinese_remainder(x: list[int], y: list[int]) -> float:
    n = len(x)
    for i in range(n):
        for j in range(n):
            if i != j:
                if gcd(y[i], y[j]) != 1:
                    return math.nan
    module = np.prod(y)
    ms = []
    m_inv = []
    for i in range(n):
        mod = 1
        for j in range(n):
            if i != j:
                mod *= y[j]
        m_ = solve_comparison_eq(mod, 1, y[i])
        ms.append(mod)
        m_inv.append(m_)
    x_ = 0
    for i in range(n):
        x_ += ms[i] * m_inv[i] * x[i]
    x %= module
    return x_
