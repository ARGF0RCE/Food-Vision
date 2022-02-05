def factorization(x):
    factors = []
    if x == 2:
        return [(1, 2)]
    else:
        for i in range(2, x):
            if x%i != 0:
                pass
            elif x%i == 0:
                factors.append((i, int(x/i)))
        return factors

def median(y):
    if len(y) % 2 != 0:
        return y[int((len(y)-1)/2)]
    else:
        return y[int(len(y)/2)]