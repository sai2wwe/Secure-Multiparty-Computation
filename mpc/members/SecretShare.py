from typing import List
from config.constants import DEFAULT_PRIME


class SecretShare:
    def __init__(self, shares: List[int], modulus: int = DEFAULT_PRIME):    
        self.shares = shares
        self.num_shares = len(shares)
        self.modulus = modulus

    def get_shares_only(self) -> List[int]:
        return [share[1] for share in self.shares]

    def get_share_owner_value(self, owner: int) -> int:
        if owner > self.num_shares:
            raise ValueError("Owner number is greater than the number of shares.")
        return self.shares[owner - 1][1]

    def __str__(self):
        return "Shamir Secret Shares ->" + str(self.shares)
