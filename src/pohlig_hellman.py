import gcd
import exp
from crt import invert_mod, crt
import sympy as sp
import timeit
import random
import matplotlib.pyplot as plt


def log_mod(g, x, n):
    """O(n) search for log_g(x) modulo n."""
    y, a = 1, 0

    if x == 1:
        return 0

    while y != x and a < n:
        y *= g
        y %= n
        a += 1

    if pow(g, a, n) != x:
        print("did not find")
        return None

    return a


def phi_n(x, p, r, n):
    """x^(p^(r-1)) mod n"""
    return pow(x, pow(p, r - 1), n)


def order(g, n):
    """order of g in Z/(n)"""
    y = 1
    for i in range(1, n + 1):
        y *= g
        y %= n
        if y == 1:
            return i

    return None


def ph(g, x, m, p, r):
    """finds log_g(x) mod m using pohlig-hellman
    for groups of prime power order.
    NB! g has to generate a group of order p^r
    for some prime p and some integer r
    """
    pi_0g = pow(g, pow(p, r - 1), m)  # g^(p^(r-1))
    a, q = 0, 1
    yi = x

    # g_inv = invert_mod(g, m)
    g_inv = pow(g, -1, m)
    for i in range(r):
        # find a_i such that pi_0(g)^{a_i} = y_i^{p^{r-i-1}}
        ai = log_mod(pi_0g, pow(yi, pow(p, r - i - 1), m), m)

        # update yi: y_{y+1} = y_i * g^{-p^i * a_i}
        yi *= pow(g_inv, q * ai, m)
        yi %= m

        # accumulate a_i
        a += ai * q
        q *= p
    return a


def pohlig_hellman_inner(g, x, m, factors):
    xi, ni = [], []
    n = sp.totient(m)
    for p, r in factors.items():
        e = int(n / pow(p, r))
        _g = pow(g, e, m)
        _x = pow(x, e, m)
        assert (
            pow(_g, pow(p, r), m) == 1
        ), "something is wrong with the order of the elements"

        _a = ph(_g, _x, m, p, r)

        assert pow(_g, _a, m) == _x, (
            f"dlog does not hold in subgroup of order {p}^{r}."
            "{_g}^{_a} = {pow(_g, _a, m)}, but we want {_x}"
        )
        xi.append(_a)
        ni.append(pow(p, r))

    return crt(xi, ni)


def pohlig_hellman(g, x, m):
    """compute the discrete log og x with base g modulo m.
    g has to generate the multiplicative group of units."""
    assert (
        gcd.gcd(g, m) == gcd.gcd(x, m) == 1
    ), f"g and x have to be invertible mod m, g = {g}, x = {x}, m = {m}"
    assert sp.is_primitive_root(
        g, m
    ), f"g has to generate the group of units, g = {g}, m = {m}"

    factors = sp.factorint(sp.totient(m))
    return pohlig_hellman_inner(g, x, m, factors)


def main():
    N = 100  # number of dlogs to compute

    primes = []
    with open("primes.txt", "r") as file:
        for line in file:
            primes.append(int(line.split(" ")[-1].strip()))

    # only use a subset of primes. should probebly select these at random
    _primes = primes[10:10000:100]
    t = []
    for p in _primes:
        factors = sp.factorint(p - 1)

        x_list = []
        g_list = []
        for g in range(2, p):
            if gcd.gcd(g, p) == 1:
                x_list.append(g)

            if gcd.gcd(g, p) == 1 and sp.is_primitive_root(g, p):
                g_list.append(g)

        # Pre-sample g, x pairs outside the timed code
        tests = [(random.choice(g_list), random.choice(x_list)) for _ in range(N)]

        def run_test():
            for g, x in tests:
                pohlig_hellman_inner(g, x, p, factors)

        _t = timeit.timeit(run_test, number=1)
        t.append(_t / N)
        # print(f"Total time for {N} runs: {t:.6f} seconds")
        # print(f"Average time per run: {t/N:.6e} seconds")

    plt.plot(_primes, t)
    plt.show()


if __name__ == "__main__":
    main()
