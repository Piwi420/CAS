import pygame
import random
import math

# Initialising pygame
pygame.init()
pygame.display.set_caption("Balloons")
icon = pygame.image.load("balloon.png")
pygame.display.set_icon(icon)

# Player
CannonIMG = pygame.image.load("cannon.png")
CannonX = 868
CannonY = 788
playerX_change = 0
playerY_change = 0

# Red Balloon
Red_BalloonIMG = pygame.image.load("balloon.png")
Red_BalloonX = random.randint(100, 1700)
Red_BalloonY = random.randint(200, 800)


def Cannon(x, y):
    screen.blit(CannonIMG, (x, y))


def Red_Balloon(x, y):
    screen.blit(Red_BalloonIMG, (x, y))


# Creating a screen
screen = pygame.display.set_mode((1800, 960))

pygame


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calls Variable Functions
    Cannon(CannonX, CannonY)
    Red_Balloon(Red_BalloonX, Red_BalloonY)

    pygame.display.update()
