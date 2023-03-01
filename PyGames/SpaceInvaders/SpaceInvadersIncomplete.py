import pygame
import random
import math

# Initialising pygame
pygame.init()

# Creating a screen
screen = pygame.display.set_mode((1800, 960))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("player.png")
playerX = 868
playerY = 788
playerX_change = 0
playerY_change = 0

# Enemy1
enemy1IMG = pygame.image.load("enemy1.png")
enemy1X = random.randint(100, 1700)
enemy1Y = random.randint(200, 800)
enemy1X_change = 0.5
enemy1Y_change = 40

# Bullet
bulletIMG = pygame.image.load("Bullet.png")
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy1(x, y):
    screen.blit(enemy1IMG, (x, y))


def isCollision(enemyX, enemy1Y, playerX, playerY):
    distance = math.sqrt((math.pow(enemy1X - bulletX, 2)) + (math.pow(enemy1Y - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def fire_bullet(playerX, playerY):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (playerX, playerY - 10))


# Game Loop
running = True
while running:

    # RBG
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        """ if Keystroke is pressed, singular
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 15
            if event.key == pygame.K_RIGHT:
                playerX += 15
            if event.key == pygame.K_UP:
                playerY -= 15
            if event.key == pygame.K_DOWN:
                playerY += 15   """

        # if Keystroke is pressed, continuous
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = +0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Changes X or Y with inputs
    playerX += playerX_change
    playerY += playerY_change

    # Player Boundary Box
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1736:
        playerX = 1736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 896:
        playerY = 896

    enemy1X += enemy1X_change

    # Enemy1 Boundary Box
    if enemy1X <= 0:
        enemy1X_change = 0.5
        enemy1Y += enemy1Y_change
    elif enemy1X >= 1736:
        enemy1X_change = -0.5
        enemy1Y += enemy1Y_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemy1X, enemy1Y, bulletX, bulletY)
    if collision:
        bulletY = playerY
        bullet_state = "ready"
        score += 1
        print(score)
        enemy1X = random.randint(100, 1700)
        enemy1Y = random.randint(200, 800)

    # Calls player function
    player(playerX, playerY)
    enemy1(enemy1X, enemy1Y)
    # Updates the display
    pygame.display.update()
