from typing import Tuple
import logging
import secrets
logging.basicConfig(level=logging.INFO)
from party import Party
from MPC import MPCAddition, MPCAverage

clients = int(input("Enter the number of participants: "))
client_values = [int(input(f"Enter the value for client {i+1}: ")) for i in range(clients)]
modulo = 1000

def sum_of_values(client_values):
    return sum(client_values)

  
def compute_share(client_value, modulu=100) -> Tuple[int]:
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

client_shares = []
for client_value in client_values:
    client_shares.append(compute_share(client_value, modulo))
    logging.info(f'The shares of client {client_value} are {client_shares[-1]}')

parties = []
client_shares_veritcal = list(zip(*client_shares))
for client_share in client_shares_veritcal:
    parties.append(Party(client_share, modulo))

mpc_addition = MPCAddition(parties=parties)
mpc_average = MPCAverage(parties=parties)
logging.info(f'The actual sum of the values is {sum_of_values(client_values)}')
logging.info(f'The computed sum of the values is {mpc_addition.compute_sum()}')
logging.info(f'The MPC average of the values is {mpc_average.compute_average()}')