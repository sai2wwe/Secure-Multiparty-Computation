"""

This File contains the implementation of Shamir's Secret Sharing Protocol.
It contains two functions:
    - generate_shares: This function generates a list of shares for a given secret using Shamir's Secret Sharing.
    - reconstruct_shares: This function reconstructs the secret from a given list of shares using Lagrange interpolation.

The implementation is based on the following steps:
    - Generate a random polynomial with a specified degree, where the constant term is the secret.
    - Evaluate the polynomial at different points to generate the shares.
    - Reconstruct the secret using Lagrange interpolation.

"""

from mpc.protocols.ShamirPrep import generate_polynomial, evaluate_polynomial
from config.constants import DEFAULT_PRIME, DEFAULT_THRESHOLD_DEGREE
from mpc.members.SecretShare import SecretShare

def generate_shares(secret, num_shares, threshold_degree=DEFAULT_THRESHOLD_DEGREE, prime=DEFAULT_PRIME):
    """
    Generate a list of shares for the given secret using Shamir's Secret Sharing.

    Args:
        secret (int): The secret to be shared.
        num_shares (int): The number of shares to generate.
        threshold_degree (int): The degree of the polynomial (k - 1, where k is the threshold).
        prime (int): A prime number larger than the secret.

    Returns:
        list: A list of (x, y) tuples representing the shares.
    """
    if secret >= prime:
        raise ValueError("Secret must be less than the prime number.")
    if threshold_degree >= num_shares:
        raise ValueError("Threshold degree must be less than the number of shares.")
    
    polynomial = generate_polynomial(secret, threshold_degree, prime)
    return SecretShare([(i, evaluate_polynomial(polynomial, i, prime)) for i in range(1, num_shares + 1)])

def reconstruct_shares(shares, prime=DEFAULT_PRIME):
    """
    Reconstruct the secret from a given list of shares using Lagrange interpolation.

    Args:
        shares (list): A list of (x, y) tuples representing the shares.
        prime (int): A prime number for modular arithmetic.

    Returns:
        int: The reconstructed secret.
    """
    total = 0

    for i, (xj, yj) in enumerate(shares):
        lagrange_coefficient = 1
        for k, (xk, _) in enumerate(shares):
            if i == k:
                continue
            lagrange_coefficient *= -xk * pow(xj - xk, -1, prime) # lagrange_coeff = (x - x0) / (xj - x0) * (x - x1) / (xj - x1) * ... * (x - xk) / (xj - xk)
            lagrange_coefficient %= prime
        total += yj * lagrange_coefficient
        total %= prime

    return total
