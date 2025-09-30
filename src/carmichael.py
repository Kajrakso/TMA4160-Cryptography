import sympy as sp  # to check if number is prime

import exp
from gcd import gcd

def is_prime_or_carmichael(n):
    for a in range(2, n):
        if gcd(a, n) == 1 and exp.exp(a, n-1, n) != 1:
            return False
    return True


def main():
    for i in range(2, 10000):
        if is_prime_or_carmichael(i) and not sp.isprime(i):
            print(i)


if __name__ == "__main__":
    main()
