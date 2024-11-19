from mpc.core import MPCAddition, MPCAverage
from mpc.party import Party
from mpc.utils import generate_secret_shares, sum_of_values
import logging

logging.basicConfig(level=logging.INFO)

def main():
    clients = int(input("Enter the number of participants: "))
    client_values = [int(input(f"Enter the value for client {i+1}: ")) for i in range(clients)]
    modulo = int(input("Enter the modulo: "))
    share_count = int(input("Enter the number of shares to be generated: "))

    client_shares = [generate_secret_shares(value, share_count, modulo) for value in client_values]
    for client_share in client_shares:
        logging.info(client_share)
    client_shares_vertical = list(zip(*client_shares))
    for client_share in client_shares_vertical:
        logging.info(client_share)
    parties = [Party(share, modulo) for share in client_shares_vertical]

    mpc_addition = MPCAddition(parties)
    mpc_average = MPCAverage(parties)

    logging.info(f"Actual sum: {sum_of_values(client_values)}")
    logging.info(f"MPC computed sum: {mpc_addition.compute()}")
    logging.info(f"MPC computed average: {mpc_average.compute()}")

if __name__ == "__main__":
    main()
