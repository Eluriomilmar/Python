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
    "A                    AD              D",
    "A              AD                    D",
    "A                                    D",
    "A                                    D",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
    "ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSD",
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

player.x = WIDTH / 2
player.y = HEIGHT / 2
velocity = 0
gravity = 1
background = Actor("background_color_mushrooms")
solid = Actor("background_solid_dirt")
backgrounds = []
backgrounds_len = 0
while backgrounds_len < 2048:
    backgrounds.append(background)
    backgrounds_len += background.width
background_offset = 0
RR = True
LR = True
original_x = player.x
original_y = player.y
debug1 = 0
debug2 = 0
on_air = False
h_velocity = 0

def move_tela(ori_x, ori_y, var):
    if var == 1:
        for wall in walls:
            wall.x += player.x - ori_x
            wall.y += player.y - ori_y
        for wall in walls_right:
            wall.x += player.x - ori_x
            wall.y += player.y - ori_y
        for wall in walls_left:
            wall.x += player.x - ori_x
            wall.y += player.y - ori_y
    if var == -1:
        for wall in walls:
            wall.x -= player.x - ori_x
            wall.y -= player.y - ori_y
        for wall in walls_right:
            wall.x -= player.x - ori_x
            wall.y -= player.y - ori_y
        for wall in walls_left:
            wall.x -= player.x - ori_x
            wall.y -= player.y - ori_y


def on_key_up(key):
    global RR, LR
    if key == keys.LEFT:
        LR = True  # Left Released
    elif key == keys.RIGHT:
        RR = True


def on_key_down(key):
    global RR, LR
    if key == keys.LEFT:
        print("left pressed")
        LR = False
    elif key == keys.RIGHT:
        print("right pressed")
        RR = False


def update():
    global velocity, gravity, RR, LR, debug1, debug2, original_x, original_y, on_air, h_velocity
    original_y = player.y
    original_x = player.x
    original_y += velocity
    if keyboard.up and on_air == False:
        original_y -= 4
    if keyboard.down and on_air == False:
        original_y += 4
    if keyboard.right and on_air == False:
        if player.image == "front":
            player.image = "rwalk_a"
        elif player.image == "rwalk_a":
            player.image = "rwalk_b"
        elif player.image == "rwalk_b":
            player.image = "rwalk_a"
        original_x += 4
        h_velocity = 4
    if keyboard.left and on_air == False:
        if player.image == "front":
            player.image = "lwalk_a"
        elif player.image == "lwalk_a":
            player.image = "lwalk_b"
        elif player.image == "lwalk_b":
            player.image = "lwalk_a"
        h_velocity = -4
        original_x -= 4
    if LR and RR:
        player.image = "front"
    if player.collidelist(walls) == -1 and player.collidelist(walls_left) == -1 and player.collidelist(walls_right) == -1:
        velocity += gravity
        on_air = True
    else:
        velocity = 0
        h_velocity = 0
        on_air = False
    if keyboard.space:
        if (player.collidelist(walls) != -1 or player.collidelist(walls_left) != -1 or
            player.collidelist(walls_right) != -1) and velocity == 0:
            velocity = -25
    if player.collidelist(walls_left):
        if player.left < walls_left[player.collidelist(walls_left)].right:
            original_x += 4
    if player.collidelist(walls_right):
        if player.right > walls_right[player.collidelist(walls_right)].left:
            original_x -= 4
    if on_air == True:
        original_x += h_velocity
    move_tela(original_x, original_y, 1)


def draw():
    for i, background in enumerate(backgrounds):
        background.left = i * 512
        background.y = 300
        background.draw()
    screen.draw.filled_rect(Rect((0, 0), (1600, 150)), (255, 255, 255))
    screen.draw.filled_rect(Rect((0, 450), (1600, 900)), (222, 126, 79))
    player.draw()
    screen.draw.rect(Rect((player.topleft[0], player.topleft[1]),
                          (player.bottomright[0] - player.topleft[0], player.bottomright[1] - player.topleft[1])),
                     (0, 0, 255))
    for wall in walls:
        wall.draw()
    for wall in walls_left:
        wall.draw()
    for wall in walls_right:
        wall.draw()


pgzrun.go()