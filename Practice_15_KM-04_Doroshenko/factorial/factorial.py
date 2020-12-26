def fact(a):
    if a == 0:
        return a
    else:
        return a*(fact(a - 1))
