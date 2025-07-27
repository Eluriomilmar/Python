import pgzrun
from pyparsing import original_text_for

WIDTH = 1600
HEIGHT = 900

# Level map (W for Wall, P for Player, G for Goal)
level_map = [
    "QWWWWWWWWWWE",
    "A          D",
    "A          D",
    "A          D",
    "A    P     D",
    "A SSSSSSSS D",
    "A          D",
    "A          D",
    "A          D",
    "ZXXXXXXXXXXC"
]

player = Actor('character_beige_idle') # Assuming 'player.png' exists # Assuming 'goal.png' exists

walls = []
for i in range(len(level_map)):
    for j in range(len(level_map[i])):
        if level_map[i][j] == "W":
            wall = Actor('terrain_grass_block_top')
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)
            print(f"wall size: {wall.size}")

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
            wall = Actor("terrain_grass_block_left")
            wall.y = i * 64 + 32
            wall.x = j * 64
            walls.append(wall)

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
            walls.append(wall)

        if level_map[i][j] == "S":
            wall = Actor("terrain_grass_block_center")
            wall.y = i * 64 + 64
            wall.x = j * 64
            walls.append(wall)

        if level_map[i][j] == "P":
            player.y = i * 64 + 32
            player.x = j * 64
velocity = 0
gravity = 1



def update():
    global velocity, gravity
    original_y = player.y
    original_x = player.x
    original_y += velocity
    if player.collidelist(walls) == -1:
        velocity += gravity
    else:
        velocity = 0
    if keyboard.space and player.collidelist(walls) != -1:
        velocity = -15
    if keyboard.up:
        original_y -= 2
    if keyboard.down:
        original_y += 2
    if keyboard.right:
        original_x += 2
    if keyboard.left:
        original_x -= 2
    for wall in walls:
        wall.x += player.x - original_x
        wall.y += player.y - original_y








def draw():
    screen.clear()
    player.draw()
    for wall in walls:
        wall.draw()





pgzrun.go()