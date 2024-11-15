from typing import Tuple
import logging
import secrets
logging.basicConfig(level=logging.INFO)



a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
modulo = 1000

def sum_of_two(a, b):
    return a + b


class Party:
    """
    Represents a party in the Multi-Party Computation (MPC).
    Attributes:
        a_share: Share of the first input.
        b_share: Share of the second input.
        modulo: Modulo value for computations.
    """
    def __init__(self, a_share, b_share, modulo) -> None:
        self.a_share = a_share
        self.b_share = b_share
        self.modulo = modulo
    
    def compute_partial_sum(self) -> int:
        return (self.a_share + self.b_share) % self.modulo

class MPCAddition:
    def __init__(self, parties):
        self.parties = parties

    def compute_sum(self) -> int:
        total_sum = sum([party.compute_partial_sum() for party in self.parties])

        return total_sum % self.parties[0].modulo
 
   
def compute_share(a, modulu=100) -> Tuple[int]:
    '''
    This function computes the shares of a number
    @param a: the number to be shared
    @return: the shares of the number Tuple(first_share, second_share, third_share)
    '''
    while True:
        first_share = secrets.randbelow(modulu)
        second_share =secrets.randbelow(modulu)
        third_share = (a - first_share - second_share) % modulu
        if third_share >= 0:
            return first_share, second_share, third_share 


def create_parties(a_shares, b_shares, modulu=100, number_of_parties=3) -> Tuple[Party]:
    '''
    This function creates the parties involved in the computation
    @param a_shares: the shares of a
    @param b_shares: the shares of b
    @return: the parties involved in the computation
    '''
    return [Party(a_shares[i], b_shares[i], modulu) for i in range(number_of_parties)] 

a_shares = compute_share(a, modulo)
b_shares = compute_share(b, modulo)
parties = create_parties(a_shares, b_shares,modulo)

mpc_addition = MPCAddition(parties=parties)

logging.info(f'The shares of a are {a_shares}')
logging.info(f'The shares of b are {b_shares}')
logging.info(f'The actual sum of {a} and {b} is {sum_of_two(a, b)}')
logging.info(f'The sum of {a} and {b} is {mpc_addition.compute_sum()}')