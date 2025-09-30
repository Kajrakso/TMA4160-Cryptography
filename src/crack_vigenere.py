import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import re
from vigenere import *

alphabet = np.array([chr(i) for i in range(ord("a"), ord("z") + 1)])


def count_letters(text):
    cnt = np.zeros(len(alphabet))
    text = np.array(list(text))

    for i, ltr in enumerate(alphabet):
        cnt[i] = (text == ltr).sum()

    return cnt


def count_matching_letters(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)


english_freq = [
    0.08167,
    0.01492,
    0.02782,
    0.04253,
    0.12702,
    0.02228,
    0.02015,
    0.06094,
    0.06966,
    0.00153,
    0.00772,
    0.04025,
    0.02406,
    0.06749,
    0.07507,
    0.01929,
    0.00095,
    0.05987,
    0.06327,
    0.09056,
    0.02758,
    0.00978,
    0.02360,
    0.00150,
    0.01974,
    0.00074,
]


def main():
    c = "rikvbiybithusevazmmltkasrnhpnpzicswdsvmbiyfqezubzpbrgyntburmbeczqkbmbpawixsofnuzecnrazfphiybqeocttioxkunohmrgcnddxzwirdvdrzyayyicpuydhckxqieciewuicjnnacsazzzgaczhmrgxftilfnntsdafgywlnicfiseamrmorpgmjlustaakbfltibyxgavdvxpctsvvrljenowwfinzowehosrmqdgysdopvxxgpjnrvilznareduybtvlidlmsxkyeyvakaybpvtdhmtmgitdzrtiovwqieceybnedpzwkundozrbahegqbxurfgmuecnpaiiyurlriptfoybiseoedzinaispbtzmnecrijufucmmuusanmmvicnrhqjmnhpncepusqdmivytsztrgxspzuvwnorgqjmynlilukcphdbylnelphvkyayybyxlermmpbmhhcqkbmhdkmtdmssjevwopngcjmyrpyqelcdpopvpbiezalkzwtopryfaratpbhglwwmxnhphxvkbaanavmnlphmemmszhmtxhtfmqvlilovvulniwgvfucgrzzkaunadvyxuddjvkayuyowlvbeozfgthhspjnkayicwitdarzpvu"

    res = []
    L = 3
    for i in range(len(c) - L):
        res.append(re.findall(c[i : i + L :], c))

    actual = []
    for _res in res:
        if len(_res) > 2:
            actual.append(_res)

    repeats = []
    for _a in actual:
        if _a[0] not in repeats:
            repeats.append(_a[0])

    # print(repeats)

    idx = [
        [m.start(0) for m in re.finditer(repeats[i], c)] for i in range(len(repeats))
    ]
    # print(idx)

    # for _idx in idx:
    #     for i in range(len(_idx) - 1):
    #         x = _idx[i + 1] - _idx[i]
    #         print(f"{x} ({sp.factorint(x)})", end=" ")
    #     print()

    # I think the key length is 7
    n = 7

    res = []
    for i in range(len(c)):
        res.append(count_matching_letters(c[:-i], c[i:]))

    # plt.bar(range(len(c)), res)
    # plt.show()

    # the key length is definitly 7...
    key = np.zeros(n)

    for i in range(len(key)):
        cnt = count_letters(c[i::n])
        key[i] = ((np.argmax(cnt) - 4) + 26) % 26

    # for _key in key:
    #     print(chr(ord('a') + int(_key)), end="")

    # key is virtual!
    key = "virtual"

    print(decode(d(encode(key), encode(c))))


if __name__ == "__main__":
    main()
