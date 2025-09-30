import pohlig_hellman

g = 6
x = 27
p = 45563183054141278586772634880035591098346241837992938175083457749195137086235079348950021950920106764545230307

a = pohlig_hellman.pohlig_hellman(g, x, p)

print()
print(f"Working in the Multiplicative group of integers mod {p}")
print()
print(f"log_{g}({x}) = {a} since\n{g}^{a} = {pow(g, a, p)}")
