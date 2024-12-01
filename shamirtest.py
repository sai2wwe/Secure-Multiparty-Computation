from mpc.protocols.ShamirSharing import generate_shares, reconstruct_shares

x = 100
prime = 2089
num_shares = 8
threshold_degree = 4

shares = generate_shares(x, num_shares, threshold_degree, prime)
print("Shares:", shares)
print("share values: ", shares.get_shares_only())
print("share values: ", shares.get_share_owner_value(1))
print('reconstructed value:', reconstruct_shares(shares.shares, prime))