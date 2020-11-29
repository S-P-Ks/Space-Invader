import pygame
from random import *
import time
import math
from PIL import Image

pygame.init()
fps = 30

# Screen Length and the Width
s_width = 800
s_height = 600
screen = pygame.display.set_mode((s_width, s_height))
icon = pygame.image.load("target.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
lost = False

# Player Image
img = pygame.image.load("s.png")
x = 350
y = 500
player_x_change = 5

# Alein Image
aliens_img = []
aliens_x = []
aliens_y = []
aliens_x_change = []
aliens_y_change = []
alien_speed = []
num_of_aliens = 5

for i in range(num_of_aliens):
    aliens_x.append(randint(0, s_width))
    aliens_y.append(randint(0, 100))
    aliens_x_change.append(10)
    aliens_y_change.append(60)
    alien_speed.append(10)
    aliens_img.append(pygame.image.load("alien.png"))

# Background Image
bg_img = pygame.image.load("d.jpg")
bg_img = pygame.transform.scale(bg_img, (800, 600))

# Bullet Image
bullet_img = pygame.image.load("bullet (1).png")
bullet_fired = False
b_x = 0
b_y = 480

# Score of a Player
score = 0
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 30)

# Show Text


def showText():
    text = myFont.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(text, (0, 0))

# Player Movement


def player():
    screen.blit(img, (x, y))

# Alien Movement


def alien(a_img, a_x, a_y):
    screen.blit(a_img, (a_x, a_y))

# Bullet Movement


def bullet(x, y):
    global b_x, b_y
    b_x = x
    b_y = y
    screen.blit(bullet_img, (x, y))
    global bullet_fired
    bullet_fired = True

# Collison Detection


def collision(a_x, a_y, b_x, b_y):
    d = math.sqrt((math.pow(a_x - b_x, 2)) + (math.pow(a_y - b_y, 2)))
    if d < 30:
        return True
    else:
        return False


screen.fill((0, 0, 0))
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_img, (0, 0))
    showText()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 5

            if event.key == pygame.K_LEFT:
                player_x_change = -5

            if event.key == pygame.K_SPACE:
                if bullet_fired == False:
                    bullet(x+32, y)

    x += player_x_change

    if b_y < 0:
        b_x = 0
        b_y = 0
        bullet_fired = False

    if bullet_fired == True:
        bullet(b_x, b_y-20)

    for i in range(num_of_aliens):
        alien(aliens_img[i], aliens_x[i], aliens_y[i])
        if not lost:
            aliens_x[i] += aliens_x_change[i]
            if aliens_x[i] < 4:
                aliens_x_change[i] = alien_speed[i]
                aliens_x[i] += aliens_x_change[i]
                aliens_y[i] += aliens_y_change[i]
            if aliens_x[i] > s_width - 64:
                aliens_y[i] += aliens_y_change[i]
                aliens_x_change[i] = -alien_speed[i]
                aliens_x[i] += aliens_x_change[i]

        if aliens_y[i] > s_height:
            lost = True
            aliens_x_change[i] = 0
            aliens_y_change[i] = 0
            print(lost)

        coll = collision(aliens_x[i], aliens_y[i], b_x, b_y)
        if coll:
            aliens_x[i] = randint(0, s_width)
            aliens_y[i] = randint(0, 100)
            aliens_x_change[i] += 20
            score += 1
            alien_speed[i] += 5
            bullet_fired = False
            print(score)

        if x > s_width-64:
            x = 734
        if x < 4:
            x = 0

    player()
    pygame.display.update()
    clock.tick(fps)
