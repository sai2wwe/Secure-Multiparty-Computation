from typing import Tuple
class Party:
    """
    Represents a party in the MPC protocol.
    acts as a party in the MPC protocol. No party has access to the actual value of the secret or the shares of the other parties.

    Attributes:
        client_shares: list of shares of the party
        modulo: the modulo value to be used for the computation
    
    Methods:
        compute_partial_sum(): computes the sum of the shares
    """
    def __init__(self, client_shares, modulo=1000) -> None:
        self.client_shares = client_shares
        self.modulo = modulo
    
    def compute_partial_sum(self) -> int:
        self.parital_sum =  sum(self.client_shares) % self.modulo
        return self.parital_sum
    
    def __str__(self) -> str:
        return f"Party(shares={self.client_shares}, modulo={self.modulo})"
    

class BeaverParty:
    """
    Represents a party in the MPC protocol using Beaver's Triple.
    Each party computes the partial product of the shares and the final product is computed by summing the partial products
    x*y = c + e*b + f*a + [e*f] where [] is computed by only one party

    Attributes:
        x_share: the share of the value x
        y_share: the share of the value y
        a_share: the share of the value a
        b_share: the share of the value b
        c_share: the share of the value c
        modulo: the modulo value to be used for the computation
    
    Methods:
        compute_partial_e_f(): computes the partial values e and f
        compute_partial_product(e, f): computes the partial product of the shares
    """
    def __init__(self, xy_shares, abc_shares, modulo):
        self.x_share, self.y_share = xy_shares
        self.a_share, self.b_share, self.c_share = abc_shares
        self.modulo = modulo

    def compute_partial_e_f(self) -> Tuple[int]:
        """
        Computes the partial values e and f using the shares of the values x, y, a, b
        e = (x - a) % modulo
        f = (y - b) % modulo

        Returns:
            Tuple[int]: the partial values e and f
        """
        e = (self.x_share - self.a_share) % self.modulo
        f = (self.y_share - self.b_share) % self.modulo
        return e, f

    def compute_partial_product(self, e, f) -> int:
        '''
        It computes the partial product of the shares.
        returns the partial product
        partial_product = c_share + e*b_share + f*a_share + [e*f]
        [] - only one party will compute this value
        '''
        print(e,f)
        term1 = self.c_share
        term2 = (e * self.b_share)
        term3 = (f * self.a_share)
        partial_product = (term1 + term2 + term3) % self.modulo
        print(f"Party: term1={term1}, term2={term2}, term3={term3}, partial_product={partial_product}")
        return partial_product

    def __str__(self):
        return f"BeaverParty(x={self.x_share}, y={self.y_share}, a={self.a_share}, b={self.b_share}, c={self.c_share})"