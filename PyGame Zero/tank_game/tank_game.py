import pgzrun
from random import randint

WIDTH=800
HEIGHT=600

tank = Actor("tank_blue")
tank.x = 400
tank.y = 575
tank.angle = 90
bullet_holdoff = 0
background = Actor("grass")
walls = []
for i in range(1, 15):
    for j in range(1, 11):
        if randint(0,100) < 50:
            wall = Actor("wall")
            wall.x = i * 50 + 25
            wall.y = j * 50 + 25
            walls.append(wall)

bullets = []


def update():
    global bullet_holdoff
    original_x = tank.x
    original_y = tank.y
    if keyboard.left:
        tank.angle = 180
        if tank.x > 21:
            tank.x -= 2
        else:
            tank.x = original_x
    elif keyboard.right:
        tank.angle = 0
        if tank.x < 779:
            tank.x += 2
        else:
            tank.x = original_x
    elif keyboard.up:
        tank.angle = 90
        if tank.y > 24:
            tank.y -= 2
        else:
            tank.y = original_y
    elif keyboard.down:
        tank.angle = 270
        if tank.y < 576:
            tank.y += 2
        else:
            tank.y = original_y
    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y
    if bullet_holdoff == 0:
        if keyboard.space:
            bullet = Actor("bulletblue2")
            bullet.angle = tank.angle
            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff = 100
    else:
        bullet_holdoff -= 1
    for bullet in bullets:
        if bullet.angle == 90:
            bullet.y -= 5
        elif bullet.angle == 270:
            bullet.y += 5
        elif bullet.angle == 180:
            bullet.x -= 5
        elif bullet.angle == 0:
            bullet.x += 5
    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                bullets.remove(bullet)



def draw():
    screen.fill((0,0,0))
    background.draw()
    for wall in walls:
        wall.draw()
    for bullet in bullets:
        bullet.draw()
    tank.draw()


pgzrun.go()