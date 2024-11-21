from mpc.utils import generate_secret_shares
from secrets import randbelow

def beavers_triples(modulus=1000):
    """
    Generates a Beaver's Triple within the given modulus

    Args:
        modulus (int): the modulo value to be used
    
    Returns:
        a, b, c: the values of the Beaver
    """
    a = randbelow(modulus)
    b = randbelow(modulus)
    c = (a * b) % modulus
    return a, b, c

def share_triples(a, b, c, num_shares, modulus):
    """
    Shares the Beaver's Triple among the parties

    Args:
        a, b, c (int): the values of the Beaver
        num_shares (int): the number of shares to split the secret into
        modulus (int): the modulo value to be used
    
    Returns:
        a_share, b_share, c_share: the shares of the Beaver
    """
    a_share = generate_secret_shares(a, num_shares, modulus)
    b_share = generate_secret_shares(b, num_shares, modulus)
    c_share = generate_secret_shares(c, num_shares, modulus)
    return a_share, b_share, c_share

