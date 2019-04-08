from fractions import Fraction
e = Fraction(0)
f = Fraction(1)
n = Fraction(1)
while True:
    d = Fraction(1) / f
    if d < Fraction(1,10**100):
        break
    e += d
    f *= n
    n += Fraction(1)

print('%.100f' %e)
