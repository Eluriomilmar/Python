import pgzrun
from random import randint

WIDTH=800
HEIGHT=600

tank = Actor("tank_blue")
tank.x = 400
tank.y = 575
tank.angle = 90
bullet_holdoff = 0
enemy_bullet_holdoff = 0
enemy = Actor("tank_red")
enemy.y = 25
enemy.x = 400
enemy.angle = 270
enemy.move_count = 0
background = Actor("grass")
walls = []
enemies = []
game_over = False
for i in range(3):
    enemy = Actor("tank_red")
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)
for i in range(1, 15):
    for j in range(1, 11):
        if randint(0,100) < 50:
            wall = Actor("wall")
            wall.x = i * 50 + 25
            wall.y = j * 50 + 25
            walls.append(wall)

bullets = []
enemy_bullets = []


def update():
    global bullet_holdoff, enemy_bullet_holdoff, game_over
    original_x = tank.x
    original_y = tank.y
    choice = randint(0,2)
    for enemy in enemies:
        if enemy_bullet_holdoff > 0:
            enemy_bullet_holdoff -= 1
        if choice == 0:
            enemy.move_count = 20
            if enemy.x > 779 or enemy.x < 20 or enemy.y > 576 or enemy.y < 24:
                if enemy.x > 779:
                    enemy.x -= 2
                if enemy.x < 20:
                    enemy.x += 2
                if enemy.y > 576:
                    enemy.y -= 2
                if enemy.y < 24:
                    enemy.y += 2
            if enemy.move_count > 0:
                enemy.move_count -= 1
                if enemy.angle == 0:
                    enemy.x += 2
                elif enemy.angle == 90:
                    enemy.y -= 2
                elif enemy.angle == 180:
                    enemy.x -= 2
                elif enemy.angle == 270:
                    enemy.x -= 2
        elif choice == 1:
            enemy.angle = randint(0,3) * 90
        elif choice == 2 and enemy_bullet_holdoff == 0:
            bullet = Actor("bulletred2")
            bullet.angle = enemy.angle
            bullet.x = enemy.x
            bullet.y = enemy.y
            enemy_bullets.append(bullet)
            enemy_bullet_holdoff = 100
    if keyboard.left:
        tank.angle = 180
        if tank.x > 20:
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
    for bullet in enemy_bullets:
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
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            del enemies[enemy_index]
            bullets.remove(bullet)
    for bullet in enemy_bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            enemy_bullets.remove(bullet)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
             enemy_bullets.remove(bullet)
        if bullet.colliderect(tank):
            game_over = True




def draw():
    if len(enemies) == 0:
        screen.fill((0,0,0))
        screen.draw.text("Vitória!!", (260,250), color=(255,255,255), fontsize=100)
    elif game_over:
        screen.fill((0,0,0))
        screen.draw.text("Derrota :(", (260,250), color=(255,255,255), fontsize=100)
    else:
        background.draw()
        for wall in walls:
            wall.draw()
        for bullet in bullets:
            bullet.draw()
        for bullet in enemy_bullets:
            bullet.draw()
        tank.draw()
        for enemy in enemies:
            enemy.draw()


pgzrun.go()