import numpy as np

modulus = 26


def encode(m):
    encoding = []
    for _m in m:
        encoding.append(ord(_m) - ord("a"))
    return encoding


def decode(encoding):
    m = ""
    for _i in encoding:
        m += chr(_i + ord("a"))
    return m


def e(k, m):
    L = len(m)
    n = len(k)
    c = m[:]
    for i in range(L):
        c[i] = (m[i] + k[i % n]) % modulus
    return c


def d(k, c):
    L = len(c)
    n = len(k)
    m = c[:]
    for i in range(L):
        m[i] = ((c[i] - k[i % n]) + modulus) % modulus
    return m


def main():
    c = "rikvbiybithusevazmmltkasrnhpnpzicswdsvmbiyfqezubzpbrgyntburmbeczqkbmbpawixsofnuzecnrazfphiybqeocttioxkunohmrgcnddxzwirdvdrzyayyicpuydhckxqieciewuicjnnacsazzzgaczhmrgxftilfnntsdafgywlnicfiseamrmorpgmjlustaakbfltibyxgavdvxpctsvvrljenowwfinzowehosrmqdgysdopvxxgpjnrvilznareduybtvlidlmsxkyeyvakaybpvtdhmtmgitdzrtiovwqieceybnedpzwkundozrbahegqbxurfgmuecnpaiiyurlriptfoybiseoedzinaispbtzmnecrijufucmmuusanmmvicnrhqjmnhpncepusqdmivytsztrgxspzuvwnorgqjmynlilukcphdbylnelphvkyayybyxlermmpbmhhcqkbmhdkmtdmssjevwopngcjmyrpyqelcdpopvpbiezalkzwtopryfaratpbhglwwmxnhphxvkbaanavmnlphmemmszhmtxhtfmqvlilovvulniwgvfucgrzzkaunadvyxuddjvkayuyowlvbeozfgthhspjnkayicwitdarzpvu"

    k = "virtual"

    # c = "aaaa"
    # k = "ab"
    print(decode(d(encode(k), encode(c))))


if __name__ == "__main__":
    main()
