import pgzrun
from random import choice
from random import randint

WIDTH=800
HEIGHT=600
ninja = Actor("run__000")
ninja.x = 100
ninja.y = 400
velocity_y = 0
gravity = 1
obstaculos = []
inimigos = ["barnacle_bite", "cactus", "slimewalk1"]
timeout_obstaculos = 0
score = 0
game_over = False

def update():
    global velocity_y, gravity, timeout_obstaculos, score, game_over
    if ninja.image == "run__000":
        ninja.image = "run__001"
    elif ninja.image == "run__001":
        ninja.image = "run__002"
    elif ninja.image == "run__002":
        ninja.image = "run__003"
    elif ninja.image == "run__003":
        ninja.image = "run__004"
    elif ninja.image == "run__004":
        ninja.image = "run__005"
    elif ninja.image == "run__005":
        ninja.image = "run__006"
    elif ninja.image == "run__006":
        ninja.image = "run__007"
    elif ninja.image == "run__007":
        ninja.image = "run__008"
    elif ninja.image == "run__008":
        ninja.image = "run__009"
    elif ninja.image == "run__009":
        ninja.image = "run__000"
    if keyboard.space:
        if ninja.y == 400:
            velocity_y = -15
    if velocity_y > 1:
        ninja.image = "glide_006"
    if ninja.y == 400 and ninja.image == "glide_006":
        ninja.image = "run__000"
    ninja.y += velocity_y
    velocity_y += gravity
    if ninja.y > 400:
        velocity_y = 0
        ninja.y = 400
    timeout_obstaculos += 1
    if timeout_obstaculos > 50:
        actor = Actor(str(choice(inimigos)))
        actor.x = 850 + randint(0,150)
        actor.y = 430
        obstaculos.append(actor)
        timeout_obstaculos = 0
    for actor in obstaculos:
        actor.x -= 8
        if actor.x < -50:
            if game_over == False:
                obstaculos.remove(actor)
                score += 1
    if ninja.collidelist(obstaculos) != -1:
        game_over = True


def draw():
    screen.draw.filled_rect(Rect(0,0,800,400), (163,232,254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88,242,152))
    if game_over:
        screen.draw.text("Game Over", centerx=400, centery=270, color=(255,255,255), fontsize=60)
        screen.draw.text("Score: " + str(score), centerx=400, centery=330, color=(255,255,255), fontsize=60)
    else:
        ninja.draw()
        for actor in obstaculos:
            actor.draw()
        screen.draw.text("Score: " + str(score), (15,10), color=(0,0,0), fontsize= 30)

pgzrun.go()