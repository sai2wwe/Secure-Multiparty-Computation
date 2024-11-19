from secrets import randbelow

def generate_polynomial(secret, threshold_degree, prime):
    return [secret] + [randbelow(prime) for _ in range(threshold_degree) ]


def evaulate_polynomial(polynomial, x, prime):
    
    total = 0
    for i, coef in enumerate(polynomial):
        total += coef * (x ** i)

    return total % prime

