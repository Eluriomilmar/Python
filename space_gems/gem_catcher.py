import pgzrun
import random
from math import sqrt

WIDTH = 800
HEIGHT = 600
score = 0
high_score = 0
game_over = False
lives = 2
embarcado = False
nave1 = Actor("playership1_blue")
nave2 = Actor("playership1_green")
nave3 = Actor("playership1_red")
nave4 = Actor("playership1_orange")
ship = Actor("hud_keyblue")
nave1.x = 450
nave1.y = 300
nave2.x = 550
nave2.y = 300
nave3.x = 250
nave3.y = 300
nave4.x = 350
nave4.y = 300


imagens = ["gemblue","gemgreen","gemred","gemyellow"]
gem = Actor(random.choice(imagens))
gem.x = random.randint(20, 780)
gem.y = 0

def update():
    global score
    global game_over
    global lives
    global embarcado
    if embarcado == True:
        if gem.y > 600:
            if lives < 1:
                game_over = True
            else:
                lives -= 1
                gem.image = str(random.choice(imagens))
                gem.x = random.randint(20, 780)
                gem.y = random.randint(0, 20)
        else:
            gem.y += sqrt(score + 1)
        if gem.colliderect(ship):
            gem.image = str(random.choice(imagens))
            gem.x = random.randint(20, 780)
            gem.y = random.randint(0, 20)
            score += 1

def on_mouse_move(pos, rel, button):
    global game_over
    if game_over == False:
        ship.x = pos[0]
        ship.y = pos[1]

def on_mouse_down(pos, button):
    global embarcado
    if ship.colliderect(nave1) and button:
        ship.image = nave1.image
        embarcado = True
    if ship.colliderect(nave2) and button:
        ship.image = nave2.image
        embarcado = True
    if ship.colliderect(nave3) and button:
        ship.image = nave3.image
        embarcado = True
    if ship.colliderect(nave4) and button:
        ship.image = nave4.image
        embarcado = True



def draw():
    global game_over
    global embarcado
    if embarcado:
        screen.fill((80,0,70))
        #screen.clear()
        if game_over:
            screen.draw.text("Game Over", (WIDTH/2 - 150, HEIGHT/2), color=(255,255,255), fontsize=60)
            screen.draw.text("Score: " + str(score), (WIDTH/2 - 100, HEIGHT/2 + 50), color=(255,255,255), fontsize=40)
        else:
            ship.draw()
            gem.draw()
            screen.draw.text("Score: " + str(score), (15, 10), color=(255, 255, 255), fontsize=30)
            screen.draw.text("Lives: " + str(lives + 1), (15, 30), color=(255,255,255), fontsize=30)
    else:
        screen.draw.text("Choose your ship", (WIDTH/2 - 150, 200), color=(255,255,255), fontsize=60)
        nave1.draw()
        nave2.draw()
        nave3.draw()
        nave4.draw()


pgzrun.go()