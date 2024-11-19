class Party:
    """
    The Party class represents a party in the MPC protocol.
    It contains the shares of the party and the modulo value.
    client_shares: list of shares of the party
    modulo: the modulo value to be used for the computation
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
    The BeaverParty class represents a party in the Beaver's Triple protocol.
    It contains the shares of the party and the modulo value.
    xy_shares: shares of the values x and y
    abc_shares: shares of the values a, b, and c
    modulo: the modulo value to be used for the computation
    """
    def __init__(self, xy_shares, abc_shares, modulo):
        self.x_share, self.y_share = xy_shares
        self.a_share, self.b_share, self.c_share = abc_shares
        self.modulo = modulo

    def compute_partial_e_f(self):
        """
        It computes the partial values e and f.
        returns: e, f
        """
        e = (self.x_share - self.a_share) % self.modulo
        f = (self.y_share - self.b_share) % self.modulo
        return e, f

    def compute_partial_product(self, e, f):
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