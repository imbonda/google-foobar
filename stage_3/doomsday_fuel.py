import numpy as np
from functools import reduce
from fractions import gcd

def solution(m):
    # Your code here
    if len(m) < 2:
        return [1, 1]
    return MarkovChain(m).get_stable_state()

class MarkovChain(object):
    def __init__(self, states):
        n = len(states)
        absorbing, transient = [], []
        sums = [[]] * n

        for i, state in enumerate(states):
            sums[i] = sum(state)
            (transient if sums[i] else absorbing).append(i)

        # Calculating the canonical form
        states = np.matrix(states, dtype=float)[transient, :]
        self.cd = np.prod(states.sum(1))
        F = states / states.sum(1)
        self.Q, self.R = F[:, transient], F[:, absorbing]

    def get_stable_state(self):
        I = np.identity(len(self.Q))
        N = (I - self.Q) ** -1
        # Denoting the absorbing probabilities matrix
        B = N * self.R * self.cd / np.linalg.det(N)
        # Simplifying the raw output
        return [i for i in self._simplify(B[0])]

    @classmethod
    def _simplify(cls, B):
        B = B.round().astype(int).A1
        B = np.append(B, B.sum())
        return B / reduce(gcd, B)


tests = [
    [],

    [
        [0]
    ],
    [
        [1]
    ],

    [
        [0, 1],
        [0, 0],
    ],
    
    [
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 1],
    ],
    [
        [0, 1, 1],
        [0, 0, 0],
        [0, 1, 0],
    ],

    [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    
    [   # output [7, 6, 8, 21]
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [   # output [0, 3, 2, 9, 14]
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
]
for t in tests:
    print(solution(t))