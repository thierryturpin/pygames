import pygame
import random

# Initialize the game for Baptiste
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space TB")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('spaceship_64.png')
PlayerX = 370
PlayerY = 480
PlayerX_change = -1

# Enemy
EnemyImg = pygame.image.load('monster.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 1
EnemyY_change = 40

def player(x, y):
    screen.blit(PlayerImg, (x, y))

def enemy(x, y):
    screen.blit(EnemyImg, (x, y))

# Game loop
running = True
while running:

    # RGB
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if keyboard arrow left or right is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -1
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 1
    # Check if keyboard is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    # Checking for boundaries
    PlayerX += PlayerX_change
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    # Checking for boundaries for the enemy
    EnemyX += EnemyX_change
    if EnemyX <= 0:
        EnemyX_change = 0.5
        EnemyY += EnemyY_change
    elif EnemyX >= 736:
        EnemyX_change = -0.5
        EnemyY += EnemyY_change

    player(PlayerX, PlayerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()