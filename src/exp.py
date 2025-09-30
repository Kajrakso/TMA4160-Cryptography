def exp_mod(x, a, n):
    """x^a (mod n)"""
    m = x
    res = 1

    while 1:
        if a & 1:
            res = (res * m) % n
        m = (m * m) % n
        a >>= 1
        if a == 0:
            break

    return res


def main():
    x = 5  # base
    a = 582  # exponent
    n = 10007  # modulus

    print(exp_mod(x, a, n))


if __name__ == "__main__":
    main()
