from secrets import randbelow
from config.constants import DEFAULT_PRIME, DEFAULT_THRESHOLD_DEGREE

def generate_polynomial(secret, threshold_degree=DEFAULT_THRESHOLD_DEGREE, prime=DEFAULT_PRIME):
    """
    Generate a random polynomial with a specified degree, where the constant term is the secret.

    Args:
        secret (int): The secret to be shared.
        threshold_degree (int): The degree of the polynomial (k - 1, where k is the threshold).
        prime (int): A prime number larger than the secret.

    Returns:
        list: Coefficients of the polynomial [a_0, a_1, ..., a_d].
    """
    if secret >= prime:
        raise ValueError("Secret must be less than the prime number.")
    return [secret] + [randbelow(prime) for _ in range(threshold_degree)]

def evaluate_polynomial(polynomial, x, prime=DEFAULT_PRIME):
    """
    Evaluate a polynomial at a given point x using modular arithmetic.

    Args:
        polynomial (list): Coefficients of the polynomial [a_0, a_1, ..., a_d].
        x (int): The point at which to evaluate the polynomial.
        prime (int): A prime number for modular arithmetic.

    Returns:
        int: The result of the polynomial evaluation mod prime.
    """
    total = 0
    for i, coef in enumerate(polynomial):
        total += coef * pow(x, i, prime)
        total %= prime
    return total
