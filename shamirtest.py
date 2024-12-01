from mpc.protocols.ShamirSharing import generate_shares, reconstruct_shares

x = 100
prime = 2089
num_shares = 8
threshold_degree = 4

shares = generate_shares(x, num_shares, threshold_degree, prime)
print("Shares:", shares)
check = reconstruct_shares(shares, shares[:threshold_degree+1])
print("Check:", check)
