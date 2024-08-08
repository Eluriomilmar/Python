import keyboard
from time import sleep


def posicao(x=5, y=5):
    for i in range(y):
        if i == 0:
            print(x*"."+"o")
        else:
            print(x*".")

x=5
y=5
z=0
while z == 0:
    if keyboard.read_key() == "up":
        y += 1
    if keyboard.read_key() == "down":
        y -= 1
    if keyboard.read_key() == "left":
        x -= 1
    if keyboard.read_key() == "right":
        x += 1
    posicao(x, y)
    if keyboard.read_key() == "x":
        break