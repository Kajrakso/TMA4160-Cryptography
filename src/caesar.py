modulus = 26


def encode(m):
    """map letters in string to list of integers {0, ..., modulus - 1}"""
    encoding = []
    for _m in m:
        encoding.append(ord(_m) - ord("a"))
    return encoding


def decode(encoding):
    """map list of integers {0, ..., modulus - 1} to string of letters"""
    m = ""
    for _i in encoding:
        m += chr(_i + ord("a"))
    return m


def e(k, m):
    """encrypt a message m using key k"""
    c = m[:]
    for i in range(len(m)):
        c[i] = (m[i] + k) % modulus
    return c


def d(k, c):
    """decrypt a ciphertext c using key k"""
    m = c[:]
    for i in range(len(c)):
        m[i] = (c[i] - k) % modulus
    return m


def main():
    c = "mbq"

    for _k in range(26):
        print(decode(d(_k, encode(c))))


if __name__ == "__main__":
    main()
