from mpc.utils import generate_secret_shares
from secrets import randbelow

def beavers_triples(modulus=1000):
    """
    This function generates the Beaver's Triple
    @param modulus: the modulo value to be used
    @return: a, b, c
    """
    a = randbelow(modulus)
    b = randbelow(modulus)
    c = (a * b) % modulus
    return a, b, c

def share_triples(a, b, c, num_shares, modulus):
    """
    This function generates the shares of the Beaver's Triple
    @param a: the value a
    @param b: the value b
    @param c: the value c
    @param num_shares: the number of shares to be generated
    @param modulus: the modulo value to be used
    @return: a_share, b_share, c_share
    """
    a_share = generate_secret_shares(a, num_shares, modulus)
    b_share = generate_secret_shares(b, num_shares, modulus)
    c_share = generate_secret_shares(c, num_shares, modulus)
    return a_share, b_share, c_share

