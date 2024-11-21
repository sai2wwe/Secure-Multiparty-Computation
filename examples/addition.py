from mpc.core import MPCAddition, MPCAverage
from mpc.party import Party
from mpc.utils import generate_secret_shares, sum_of_values
from config.constants import DEFAULT_MODULUS, DEFAULT_NUM_SHARES

no_clients = int(input("Enter the number of participants: "))
client_values = [int(input(f"Enter the value for client {i+1}: ")) for i in range(no_clients)]
modulus = int(input(f"Enter the modulo (Default {DEFAULT_MODULUS}): ") or DEFAULT_MODULUS)
share_count = int(input(f"Enter the number of shares to be generated (Default {DEFAULT_NUM_SHARES}): ") or DEFAULT_NUM_SHARES)

client_shares = [generate_secret_shares(value, share_count, modulus) for value in client_values]
client_shares_vertical = list(zip(*client_shares))

parties = [Party(share, modulus) for share in client_shares_vertical]

mpc_addition = MPCAddition(parties)
mpc_average = MPCAverage(parties)

print(f"Actual sum: {sum_of_values(client_values)}")
print(f"MPC computed sum: {mpc_addition.compute()}")
print(f'MPC Computed Average: {mpc_average.compute()}')
