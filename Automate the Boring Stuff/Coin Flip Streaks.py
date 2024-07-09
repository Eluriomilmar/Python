"""Coin Flip Streaks"""


import random

HH = 0
TT = 0
for a in range(10000):
    letras = "HT"
    vetor = []
    H = 0
    T = 0
    for i in range(100):
        vetor.append(random.choice(letras))

    for i in vetor:
        if i == "H":
            T = 0
            H += 1
            if H == 6:
                HH += 1
        if i == "T":
            H = 0
            T += 1
            if T == 6:
                TT += 1

print(f"HH: {HH}\nTT: {TT}")
