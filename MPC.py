class MPC:
    def __init__(self, parties):
        self.parties = parties
    
    def get_party(self, index):
        return self.parties[index]

class MPCAddition(MPC):
    def __init__(self, parties) -> None:
        super().__init__(parties)
        # TODO: Implement the continuation

    def compute_sum(self) -> int:
        total_sum = sum([party.compute_partial_sum() for party in self.parties])

        return total_sum % self.parties[0].modulo
 

class MPCAverage(MPCAddition):
    def __init__(self, parties) -> None:
        super().__init__(parties)

    def compute_average(self) -> int:
        return self.compute_sum() / len(self.parties)

 