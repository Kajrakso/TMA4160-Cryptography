import gcd


def invert_mod(x, n):
    """invert x modulo n"""
    d, y, _ = gcd.gcd_ext(x, n)

    if d != 1:
        print(x, "is not invertible modulo", n)
        return None

    return (y + n) % n


def crt(xi, ni):
    """xi: list of rhs. ni: list of moduli.
    must have (ni, nj) = 0 for i != j"""
    assert len(xi) == len(ni), "ni and xi have to have the same length"

    N = 1
    for _ni in ni:
        N *= _ni

    X = 0
    for i in range(len(ni)):
        # N is the product of the ni-s,
        # so it is divisible by all the ni-s
        Ni = N // ni[i]         # important: use // and not /

        _y = invert_mod(Ni, ni[i])
        X += Ni * _y * xi[i]

    result = X % N
    if result - int(result) != 0:
        return None

    return int(result)


def main():
    x = [1, 2, 0, 8, 101]
    n = [2, 3, 5, 11, 17]
    X = crt(x, n)
    for _x, _n in zip(x, n):
        print(X % _n, _x % _n)


if __name__ == "__main__":
    main()
