from typing import Tuple
from mpc.party import Party
import secrets


def sum_of_values(client_values):
    return sum(client_values)


def generate_secret_shares(secret, num_shares=3, modulus=1000) -> Tuple[int]:
    '''
    This function generates the shares of a secret
    @param secret: the value to be shared
    @param num_shares: the number of shares to split the secret into
    @param modulus: the modulus for the shares (default is 1000)
    @return: a list containing the shares of the secret
    '''
    partial_shares = [secrets.randbelow(modulus) for _ in range(num_shares - 1)]
    last_share = (secret - sum(partial_shares)) % modulus
    return partial_shares + [last_share]


def reconstruct_value(shares, modulu=1000):
    '''
    This function reconstructs the value from the shares
    @param shares: the shares of the number
    @return: the reconstructed value
    '''
    return sum(shares) % modulu


def create_parites(client_shares, modulo=1000):
    '''
    This function creates the parties for the MPC
    @param client_shares: the shares of the client
    @param modulo: the modulo to be used
    @return: the parties
    '''
    parties = []
    for client_share in client_shares:
        parties.append(Party(client_share, modulo))
    return parties