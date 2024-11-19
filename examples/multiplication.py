from mpc.protocols.beavers import beavers_triples, share_triples
from mpc.utils import generate_secret_shares
from mpc.party import BeaverParty
from mpc.core import MPCMultiplication

modulus = 1000
num_shares = 2

a, b, c = beavers_triples(modulus)
a_share, b_share, c_share = share_triples(a, b, c, num_shares, modulus)

x, y = int(input("enter the value of x: ")), int(input("enter the value of y: "))
x_shares = generate_secret_shares(x, num_shares, modulus)
y_shares = generate_secret_shares(y, num_shares, modulus)

beaver_parties = [
    BeaverParty([x_shares[i], y_shares[i]], [a_share[i], b_share[i], c_share[i]], modulus)
    for i in range(num_shares)
]

final_product= MPCMultiplication(beaver_parties).compute() 
print(f"Final product={final_product}, expected={(x * y) % modulus}")
assert final_product == (x * y) % modulus, "Final product mismatch"
