from mpc.utils import generate_secret_shares
class VirtualClient:
    """
    A VirtualClient is a client that acts as a party in the MPC protocol.
    owner_id: the id of the owner of the VirtualClient
    value: the value of the VirtualClient

    """
    def __init__(self, owner_id, value):
        self.owner_id = owner_id
        self.value = value
        self.client_shares = []

    def get_share(self, owner_id,value):
        """
        This function accepts the shares from other VirtualClients
        """
        self.client_shares.append((owner_id, value))

    def share(self, num_shares=3, modulus=1000):
        """
        This function generates the shares of the VirtualClient
        @return: the shares of the VirtualClient
        """
        return generate_secret_shares(self.value, num_shares, modulus)

    def __str__(self):
        return f"VirtualClient(owner_id={self.owner_id}, value={self.value})"
    

class SecretShare:
    """
    The SecretShare class represents a share of a secret.
    It contains the owner_id and the value of the share.
    owner_id: the id of the owner of the share
    value: the value of the share
    """
    def __init__(self, owner_id, value):
        self.owner_id = owner_id
        self.value = value

    def __str__(self):
        return f"SecretShare(owner_id={self.owner_id}, value={self.value})"