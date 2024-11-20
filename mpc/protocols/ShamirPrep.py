from secrets import randbelow
from config.constants import DEFAULT_PRIME, DEFAULT_THRESHOLD_DEGREE

def generate_polynomial(secret, threshold_degree = DEFAULT_THRESHOLD_DEGREE, prime=DEFAULT_PRIME):
    return [secret] + [randbelow(prime) for _ in range(threshold_degree) ]


def evaulate_polynomial(polynomial, x, prime = DEFAULT_PRIME):
    
    total = 0
    for i, coef in enumerate(polynomial):
        total += coef * (x ** i)

    return total % prime

