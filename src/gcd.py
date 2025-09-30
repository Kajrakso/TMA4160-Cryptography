def gcd(a, b):
    r0, r1 = a, b

    while r1 != 0:
        r1, r0 = r0 % r1, r1

    return r0


def gcd_ext(a, b):
    """return the gcd as well as bézout coefficients x, y s.t. ax + by = gcd(a, b)"""
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r1, r0 = r0 - r1*q, r1
        s1, s0 = s0 - s1*q, s1
        t1, t0 = t0 - t1*q, t1

    return r0, s0, t0


def main():
    a, b = 240, 46
    g, x, y = gcd_ext(a, b)

    print("gcd(", a, ",", b, ") = ", g)
    print(f"{g} = {a}*({x}) + {b}*({y})")


if __name__ == "__main__":
    main()
