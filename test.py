from mpc.utils import compute_share, reconstruct_value
from secrets import randbelow
import secrets
x = 20
y = 30

x_shares = compute_share(x, 1000)
y_shares = compute_share(y, 1000)

def beavers_triples():
    a = [randbelow(1000) for _ in range(3)]
    b = [randbelow(1000) for _ in range(3)]
    c = a * b
    return a, b, c


def generate_secret_shares(secret, num_shares=3, modulus=1000):
    '''
    This function generates the shares of a secret
    @param secret: the value to be shared
    @param num_shares: the number of shares to split the secret into
    @param modulus: the modulus for the shares (default is 1000)
    @return: a list containing the shares of the secret
    '''
    partial_shares = [secrets.randbelow(modulus) for _ in range(num_shares - 1)]
    # Calculate the final share to ensure the sum of shares equals the secret % modulus
    last_share = (secret - sum(partial_shares)) % modulus

    # Return the shares as a list
    return partial_shares + [last_share]


t_shares = generate_secret_shares(980, 4, 1000)
print(t_shares)
print(reconstruct_value(t_shares, 1000))