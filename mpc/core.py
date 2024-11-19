from typing import List
from mpc.party import Party, BeaverParty
class MPC:
    def __init__(self, parties: List[Party] | List[BeaverParty]) -> None:
        self.parties = parties
    
    def get_party(self, index):
        return self.parties[index]

class MPCAddition(MPC):
    def compute(self) -> int:
        total_sum = sum([party.compute_partial_sum() for party in self.parties])

        return total_sum % self.parties[-1].modulo
 

class MPCAverage(MPCAddition):
    def compute(self) -> int:
        return super().compute() / len(self.parties)

 
class MPCMultiplication(MPC):
    def __init__(self, parties: List[BeaverParty]) -> None:
        super().__init__(parties)
        self.e, self.f = None, None
        self.product_shares = []

    def compute_ef_shares(self) -> int:
        e_shares, f_shares = [], []
        for i, party in enumerate(self.parties):
            e, f = party.compute_partial_e_f()
            e_shares.append(e)
            f_shares.append(f)

        self.e = sum(e_shares) % self.parties[-1].modulo
        self.f = sum(f_shares) % self.parties[-1].modulo

    def compute(self):
        """
        This function computes the product of the shares
        returns: the product of the shares

        """
        self.compute_ef_shares()
        for party in self.parties:
            product = party.compute_partial_product(self.e, self.f)
            self.product_shares.append(product)  
        
        final_product = sum(self.product_shares)
        final_product = (final_product + (self.e * self.f)) % self.parties[-1].modulo

        return final_product

