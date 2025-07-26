import pgzrun

WIDTH = 1600
HEIGHT = 900
camera_x = 0
camera_y = 0

# Level map (W for Wall, P for Player, G for Goal)
level_map = [
    "WWWWWWWWWWWW",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W          W",
    "W         PW",
    "WWWWWWWWWWWW"
]

walls = []

TILE_SIZE = 40

player = Actor('character_beige_climb_a', (TILE_SIZE * 2, TILE_SIZE * 2)) # Assuming 'player.png' exists # Assuming 'goal.png' exists

def update():
    global camera_x, camera_y
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        for j, row in enumerate(level_map):
            for i, tile in enumerate(row):
                screen.draw.filled_rect(Rect((x * TILE_SIZE + 5), (TILE_SIZE, TILE_SIZE)), (100,100,100))
        player.y += 5
    camera_x = player.x
    camera_y = player.y
    for y, row in enumerate(level_map):
        for x, tile in enumerate(row):
            if tile == 'W':
                screen.draw.filled_rect(Rect((x * TILE_SIZE, y * TILE_SIZE), (TILE_SIZE, TILE_SIZE)), (100, 100, 100))


def draw():
    screen.clear()
    player.draw()





pgzrun.go()