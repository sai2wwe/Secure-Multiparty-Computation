from mpc.protocols.ShamirPrep import generate_polynomial, evaulate_polynomial
from config.constants import DEFAULT_PRIME, DEFAULT_THRESHOLD_DEGREE

def generate_shares(secret, num_shares, threshold_degree = DEFAULT_THRESHOLD_DEGREE, prime = DEFAULT_PRIME):
    """
    This funcion returns a list of shares of the secret. Each share is a tuple (x, y) 
    where x is the share number and y is the share value.
    @param secret: The secret to be shared
    @param num_shares: The number of shares to generate
    @param threshold_degree: The minimum number of shares required to reconstruct the secret
    @param prime: A prime number greater than the secret
    @return: A list of shares
    """
    polynomial = generate_polynomial(secret, threshold_degree, prime)
    return [(i, evaulate_polynomial(polynomial, i, prime)) for i in range(1, num_shares + 1)]


def reconstruct_shares(x, shares, prime = DEFAULT_PRIME):
    total = 0

    for i, (xj, yj) in enumerate(shares):
        numerator, denominator = 1, 1
        for j, (xk, _) in enumerate(shares):
            if i == j:
                continue
            numerator *= -xk
            denominator *= (xj - xk)
        total += yj * numerator * pow(denominator, -1, prime)

    return total % prime