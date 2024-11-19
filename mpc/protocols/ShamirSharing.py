from mpc.protocols.ShamirPrep import generate_polynomial, evaulate_polynomial

def generate_shares(secret, num_shares, threshold_degree, prime):
    polynomial = generate_polynomial(secret, threshold_degree, prime)
    return [(i, evaulate_polynomial(polynomial, i, prime)) for i in range(1, num_shares + 1)]


def reconstruct_shares(x, shares, prime):
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