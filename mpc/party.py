class Party:
    def __init__(self, client_shares, modulo=1000) -> None:
        self.client_shares = client_shares
        self.modulo = modulo
    
    def compute_partial_sum(self) -> int:
        self.parital_sum =  sum(self.client_shares) % self.modulo
        return self.parital_sum