from Crypto.Math._IntegerGMP import IntegerGMP
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Math.Numbers import Integer
from Crypto.Random import random, get_random_bytes
from config.constants import DEFAULT_MODULUS


class ObliviousTransfer:
    def __init__(self, curve='P-256', k0=None, k1=None):
        self.curve = curve
        self.base_point = ECC.generate(curve=curve).pointQ
        self.order = 1000
        self.k0 = k0
        self.k1 = k1
        self.p0, self.p1 = self._get_po_p1()

    def _get_po_p1(self):
        k0 = self.k0 or random.randint(1, self.order)
        k1 = self.k1 or random.randint(1, self.order)
        p0 = k0 * self.base_point
        p1 = k1 * self.base_point
        return p0, p1

    def sub_points(self, p1: ECC.EccPoint, p2: ECC.EccPoint):  # p1 - p2 = p1 + (-p2)
        print(f'Before sub:')
        print(f'p1: {p1.x}, {p1.y}')
        print(f'p2: {p2.x}, {p2.y}')
        p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
        neg_y = IntegerGMP(-1 * int(p2.x)) % p
        neg_p2 = ECC.EccPoint(p2.x, neg_y, self.curve)

        print(f'after sub:')
        # print(f'p2: {neg_p2.x}, {neg_p2.y}')
        # result = p1 + neg_p2
        # print(f'result: {result.x}, {result.y}')7
        print(f'type: {neg_y}')


def recv_calculations(ot_instance: ObliviousTransfer, choice_bit=0):
    recv_m = random.randint(1, ot_instance.order)
    u = [0] * 2
    if choice_bit == 0:
        u[0] = recv_m * ot_instance.base_point
        ub = u[0] - ot_instance.p0
        u[1] = ot_instance.p1 - ub
    return u


def send_reply(ot_instance: ObliviousTransfer, u, m0, m1):
    a0 = random.randint(1, ot_instance.order)
    a1 = random.randint(1, ot_instance.order)

    v0 = a0 * ot_instance.base_point
    v1 = a1 * ot_instance.base_point
    w0 = a0 * u[0]
    w1 = a1 * u[1]

    print(m0, m1)
    print(w0)
    print(w1)

    return v0, v1


m0, m1 = "Secret 0", "Secret 1"
choice_bit = 1
ot = ObliviousTransfer()
ot.sub_points(ot.p1, ot.p0)

# u = recv_calculations(ot)
# send_reply(ot, u, m0, m1)
