from mpc.core import MPCAddition, MPCAverage
from mpc.party import Party
from mpc.utils import generate_secret_shares, sum_of_values
from mpc.protocols.ShamirSharing import generate_shares, reconstruct_shares
from config.constants import DEFAULT_MODULUS, DEFAULT_NUM_SHARES


x = int(input("Enter the first number to compare: "))
y = int(input("Enter the second number to compare: "))

print("Offline phase: Generating shares for the numbers...")
x_shares = generate_shares(x, DEFAULT_NUM_SHARES)
y_shares = generate_shares(y, DEFAULT_NUM_SHARES)
print("Shares generated successfully.")
print(f'Shares for {x}: {x_shares}')
print(f'Shares for {y}: {y_shares}')

print("Online phase: Adding the numbers with a random number...")
rnd_num = 10
print(f'Random number: {rnd_num}')
x_shares_values = [share[1] for share in x_shares]

print(x_shares_values)