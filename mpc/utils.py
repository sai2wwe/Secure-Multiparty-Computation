from typing import Tuple
from mpc.party import Party
import secrets


def sum_of_values(client_values):
    return sum(client_values)


def generate_secret_shares(secret, num_shares=3, modulus=1000) -> Tuple[int]:
    """
    Generate secret shares of a number into num_shares within the modulus

    Args:
        secret (int): the secret to be shared
        num_shares (int): the number of shares to split the secret into
        modulus (int): the modulo value to be used

    Returns:
        List[int]: the secret shares [s1, s2, ..., sn]
    """
    partial_shares = [secrets.randbelow(modulus) for _ in range(num_shares - 1)]
    last_share = (secret - sum(partial_shares)) % modulus
    return partial_shares + [last_share]


def reconstruct_value(shares, modulus=1000):
    """
    Reconstruct the secret from the shares with the given modulus

    Args:
        shares (List[int]): the shares to be reconstructed
        modulus (int): the modulo value to be used

    Returns:
        int: the reconstructed secret [sigma(si) % modulus
    """
    return sum(shares) % modulus


def create_parties(client_shares, modulo=1000):
    """
    Creates a list of parties from the client shares with the given modulo

    Args:
        client_shares (List[int]): the shares to be used to create the parties
        modulo (int): the modulo value to be used

    Returns:
        List[Party]: the list of parties (Each party is an instance of the Party class)
    """
    parties = []
    for client_share in client_shares:
        parties.append(Party(client_share, modulo))
    return parties
