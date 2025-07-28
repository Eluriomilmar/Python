import keyboard
import pgzrun
from pyparsing import original_text_for

WIDTH = 1600
HEIGHT = 900

level_map = [
    "QWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWE",
    "A                                    D",
    "A                                    D",
    "A                                    D",
    "A                                    D",
    "A                    SSS             D",
    "A                                    D",
    "A                                    D",
    "A                                    D",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXC",
]

player = Actor("front")


walls = []
walls_right = []
walls_left = []
for i in range(len(level_map)):
    for j in range(len(level_map[i])):
        if level_map[i][j] == "W":
            wall = Actor('terrain_grass_block_top')
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "Q":
            wall = Actor("terrain_grass_block_top_left")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "E":
            wall = Actor("terrain_grass_block_top_right")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "A":
            wall = Actor('terrain_grass_block_left')
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls_left.append(wall)

        if level_map[i][j] == "Z":
            wall = Actor("terrain_grass_block_bottom_left")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "X":
            wall = Actor("terrain_grass_block_bottom")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "C":
            wall = Actor("terrain_grass_block_bottom_right")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "D":
            wall = Actor("terrain_grass_block_right")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls_right.append(wall)

        if level_map[i][j] == "S":
            wall = Actor("terrain_grass_block_center")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

player.x = WIDTH/2
player.y = HEIGHT/2
velocity = 0
gravity = 1
background = Actor("background_color_mushrooms")
solid = Actor("background_solid_dirt")
backgrounds = []
backgrounds_len = 0
while backgrounds_len < 2048:
    backgrounds.append(background)
    backgrounds_len += background.width
RR = True
LR = True
def on_key_up(key):
    global RR, LR
    if key == keys.LEFT:
        LR = True #Left key Released
    elif key == keys.RIGHT:
        RR = True #Right key Released

def on_key_down(key):
    global RR, LR
    if key == keys.LEFT:
        LR = False
    elif key == keys.RIGHT:
        RR = False




def update():
    global velocity, gravity, RR, LR
    original_y = player.y
    original_x = player.x
    original_y += velocity
    if keyboard.up:
        original_y -= 4
    if keyboard.down:
        original_y += 4
    if keyboard.right:
        if player.image == "front":
            player.image = "rwalk_a"
        elif player.image == "rwalk_a":
            player.image = "rwalk_b"
        elif player.image == "rwalk_b":
            player.image = "rwalk_a"
        original_x += 4
    if keyboard.left:
        if player.image == "front":
            player.image = "lwalk_a"
        elif player.image == "lwalk_a":
            player.image = "lwalk_b"
        elif player.image == "lwalk_b":
            player.image = "lwalk_a"
        original_x -= 4
    if LR and RR:
        player.image = "front"

    for wall in walls:
        wall.x += player.x - original_x
        wall.y += player.y - original_y
    for wall in walls_right:
        wall.x += player.x - original_x
        wall.y += player.y - original_y
    for wall in walls_left:
        wall.x += player.x - original_x
        wall.y += player.y - original_y
    if player.collidelist(walls) == -1:
        velocity += gravity
    else:
        velocity = 0
    if keyboard.space and (player.collidelist(walls) != -1):
        velocity = -25
    if player.collidelist(walls_left) != -1:
        for wall in walls:
            wall.x -= 4
        for wall in walls_left:
            wall.x -= 4
        for wall in walls_right:
            wall.x -= 4
    if player.collidelist(walls_right) != -1:
        for wall in walls:
            wall.x += 4
        for wall in walls_left:
            wall.x += 4
        for wall in walls_right:
            wall.x += 4


def draw():
    for i, background in enumerate(backgrounds):
        background.left = i * 512
        background.y = 300
        background.draw()
    screen.draw.filled_rect(Rect((0,0),(1600,150)),(255,255,255))
    screen.draw.filled_rect(Rect((0,450),(1600,900)),(222,126,79))
    player.draw()
    screen.draw.rect(Rect((player.topleft[0],player.topleft[1]),(player.bottomright[0]-player.topleft[0],player.bottomright[1]-player.topleft[1])),(0,0,255))
    for wall in walls:
        wall.draw()
    for wall in walls_left:
        wall.draw()
    for wall in walls_right:
        wall.draw()






pgzrun.go()