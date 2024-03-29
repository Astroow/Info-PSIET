import numpy as np

SYS = [1, 3, 4]

TAB = np.array([[0, 0, 0],
                [1, 1, 1],
                [2, 2, 2],
                [3, 1, 1],
                [4, 2, 1],
                [5, 3, 2],
                [6, 2, 2]])


def rendu_bas_haut(S: int, M: list) -> (int, np.array):
    T = np.zeros((S + 1, len(M)), dtype=int)
    for i in range(S + 1):
        T[i, 0] = i
    for j in range(1, len(M)):
        for i in range(S + 1):
            if M[j] <= i:
                T[i, j] = min(1 + T[i - M[j], j], T[i, j - 1])
            else:
                T[i, j] = T[i, j - 1]
    return T[S, len(M) - 1], T


def rendu_bas_haut_reconst(S: int, M: list) -> list:
    R = []
    _, T = rendu_bas_haut(S, M)
    i, j = np.shape(T)[0] - 1, np.shape(T)[1] - 1
    while T[i, j] != 0:
        if j != 0 and T[i, j] == T[i, j - 1]:
            j -= 1
        else:
            R.append(M[j])
            i -= M[j]
    return R


def rendu_rec(S: int, M: list) -> int:
    i = S
    if len(M) == 1:
        return i
    j = M[len(M) - 1]
    if j <= i:
        return min(1 + rendu_rec(i - j, M), rendu_rec(i, M[:len(M) - 1]))
    return rendu_rec(i, M[:len(M) - 1])


MEMO = {}


def rendu_dyn_memo(S: int, M: list) -> int:
    i = S
    if len(M) == 1:
        return i
    j = M[len(M) - 1]
    if (i, j) in MEMO:
        return MEMO[(i, j)]
    if j <= i:
        MEMO[(i, j)] = min(1 + rendu_dyn_memo(i - j, M), rendu_dyn_memo(i, M[:len(M) - 1]))
        return MEMO[(i, j)]
    MEMO[(i, j)] = rendu_dyn_memo(i, M[:len(M) - 1])
    return MEMO[(i, j)]
