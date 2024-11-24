from mpc.core import MPCAddition, MPCAverage
from mpc.party import Party
from mpc.utils import generate_secret_shares, sum_of_values
from config.constants import DEFAULT_MODULUS, DEFAULT_NUM_SHARES

def mpc_addition(client_values, modulus, share_count):
    client_shares = [generate_secret_shares(value, share_count, modulus) for value in client_values]
    client_shares_vertical = list(zip(*client_shares))

    parties = [Party(share, modulus) for share in client_shares_vertical]

    mpc_addition = MPCAddition(parties)
    mpc_average = MPCAverage(parties)

    print(f"Actual sum: {sum_of_values(client_values)}")
    print(f"MPC computed sum: {mpc_addition.compute()}")
    print(f'MPC Computed Average: {mpc_average.compute()}')
