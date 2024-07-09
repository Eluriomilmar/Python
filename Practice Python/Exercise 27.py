def play_x():
    x = int(input("Player 1 Specify row: "))
    y = int(input("Player 1 Specify col: "))
    table[x][y] = "x"


def play_O():
    x = int(input("Player 2 Specify row: "))
    y = int(input("Player 2 Specify col: "))
    table[x][y] = "O"


global table
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(9):
    for j in range(3):
        print(table[j])
    if i%2 == 0:
        play_x()
    else:
        play_O()