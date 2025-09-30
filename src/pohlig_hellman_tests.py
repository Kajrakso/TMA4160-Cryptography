from pohlig_hellman import ph, pohlig_hellman
import sympy

def gen_tests():
    # generates a list of test cases using the format:
    # (g, mod, x, log_g(x), p, r)
    tests = []

    m = 17          # 2**4 + 1
    g = 3
    p_n = m - 1     # 2**4 = 16
    p, r = 2, 4
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, p, r))

    m = 17          # 2**4 + 1
    g = 11
    p_n = m - 1     # 2**4 = 16
    p, r = 2, 4
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, p, r))

    m = 17          # 2**4 + 1
    g = 10
    p_n = m - 1     # 2**4 = 16
    p, r = 2, 4
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, p, r))

    m = 257         # 2**8 + 1
    g = 3
    p_n = m - 1
    p, r = 2, 8
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, p, r))

    m = 2003
    g = 5
    p_n = sympy.totient(m)
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, None, None))

    m = 2027
    g = 2
    p_n = sympy.totient(m)
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, None, None))

    m = 2029
    g = 2
    p_n = sympy.totient(m)
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, None, None))


    m = 27
    g = 5
    p_n = sympy.totient(m)
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, None, None))

    m = 27
    g = 20
    p_n = sympy.totient(m)
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, None, None))

    m = 65537
    g = 3
    p_n = m - 1     # 2**(2**4) = 2**16 = 65536
    p, r = 2, 2**4
    for i in range(m):
        tests.append((g, m, pow(g, i, m), i % p_n, p, r))

    return tests

def run_tests(tests):

    for g, m, x, expected, p, r in tests:

        try:
            result = pohlig_hellman(g, x, m)
        except Exception as e:
            result = f"error: {e}"

        if expected is None:
            if result is not None:
                print(f"  ❌ expected failure, got {result}")
        else:
            if result != expected:
                print(f"  ❌ expected {expected}, got {result}")

    print("tests finished")


if __name__ == "__main__":
    tests = gen_tests()
    run_tests(tests)

