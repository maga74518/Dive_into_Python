from math import gcd

def reduce(fract):
    div = gcd(*fract)
    return fract[0] // div, fract[1] // div

def summ(a, b):
    if a[1] == b[1]:
        return reduce((a[0] + b[0], b[1]))
    return reduce(((a[0] * b[1]) + (b[0] * a[1]), a[1] * b[1]))

def mult(a, b):
    return reduce((a[0] * b[0], a[1] * b[1]))

user_fract1 = input('дробь вида “a/b”: ').split('/')
user_fract2 = input('дробь вида “a/b”: ').split('/')

fract1 = tuple(map(int, user_fract1))
fract2 = tuple(map(int, user_fract2))

print(summ(fract1, fract2), mult(fract1, fract2))
