class Party:
    def __init__(self, a_share, b_share, modulo) -> None:
        self.a_share = a_share
        self.b_share = b_share
        self.modulo = modulo
    
    def compute_partial_sum(self) -> int:
        return (self.a_share + self.b_share) % self.modulo
    