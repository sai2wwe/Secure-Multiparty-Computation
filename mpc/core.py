class MPC:
    def __init__(self, parties):
        self.parties = parties
    
    def get_party(self, index):
        return self.parties[index]

class MPCAddition(MPC):
    def compute_sum(self) -> int:
        total_sum = sum([party.compute_partial_sum() for party in self.parties])

        return total_sum % self.parties[-1].modulo
 

class MPCAverage(MPCAddition):
    def compute_average(self) -> int:
        return self.compute_sum() / len(self.parties)

 