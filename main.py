from mpc.core import MPCAddition, MPCAverage
from mpc.party import Party
from mpc.utils import compute_share, sum_of_values
import logging

logging.basicConfig(level=logging.INFO)

def main():
    clients = int(input("Enter the number of participants: "))
    client_values = [int(input(f"Enter the value for client {i+1}: ")) for i in range(clients)]
    modulo = 1000

    client_shares = [compute_share(value, modulo) for value in client_values]
    parties = [Party(share, modulo) for share in zip(*client_shares)]

    mpc_addition = MPCAddition(parties)
    mpc_average = MPCAverage(parties)

    logging.info(f"Actual sum: {sum_of_values(client_values)}")
    logging.info(f"MPC computed sum: {mpc_addition.compute_sum()}")
    logging.info(f"MPC computed average: {mpc_average.compute_average()}")

if __name__ == "__main__":
    main()
