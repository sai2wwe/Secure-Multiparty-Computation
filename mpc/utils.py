from typing import Tuple
import secrets
def sum_of_values(client_values):
    return sum(client_values)

  
def compute_share(client_value, modulu=1000) -> Tuple[int]:
    '''
    This function computes the shares of a number
    @param a: the number to be shared
    @return: the shares of the number Tuple(first_share, second_share, third_share)
    '''
    while True:
        first_share = secrets.randbelow(modulu)
        second_share =secrets.randbelow(modulu)
        third_share = (client_value - first_share - second_share) % modulu
        if third_share >= 0:
            return first_share, second_share, third_share 

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