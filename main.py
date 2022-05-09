import networkx as nx
import pygame
import movement as move1
import Camera
import Scene
import data
import numpy as np

divideRatio = 6


def loadScene():
    file = open("C:\\xampp\\htdocs\\projekt\\camera\\scene.txt", "r")

    points = []
    walls = []

    fileLines = file.readlines()

    for i in range(len(fileLines)):
        fileLine = fileLines[i]

        if fileLine != "\n":
            x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 = fileLine.replace("\n", "").split(";")

            p1 = data.Point()
            p1.vector = [float(x1), float(y1), float(z1), 1.0]

            p2 = data.Point()
            p2.vector = [float(x2), float(y2), float(z2), 1.0]

            p3 = data.Point()
            p3.vector = [float(x3), float(y3), float(z3), 1.0]

            p4 = data.Point()
            p4.vector = [float(x4), float(y4), float(z4), 1.0]

            wall = data.Wall([p1, p2, p3, p4])

            walls.append(wall)
            wall.splitWall(divideRatio)

    splittedWalls = [i.splitedList for i in walls]

    return points, list(np.concatenate(splittedWalls).flat)


screen = pygame.display.set_mode((700, 700))
camera = Camera.Camera(700, 700, 0, 200)

points, walls = loadScene()
scene = Scene.Scene(walls, camera, screen, divideRatio)
scene.project()

move = move1.movement(scene, camera)

pygame.display.init()
pygame.display.update()
clock = pygame.time.Clock()
run = True

while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        move.moveDown()
    elif keys[pygame.K_UP]:
        move.moveUp()
    elif keys[pygame.K_RIGHT]:
        move.moveRight()
    elif keys[pygame.K_LEFT]:
        move.moveLeft()
    elif keys[pygame.K_QUOTE]:
        move.moveForward()
    elif keys[pygame.K_SEMICOLON]:
        move.moveBackward()
    elif keys[pygame.K_COMMA]:
        move.rotateXUp()
    elif keys[pygame.K_PERIOD]:
        move.rotateXDown()
    elif keys[pygame.K_p]:
        move.zoomOut()
    elif keys[pygame.K_o]:
        move.zoomIn()
    elif keys[pygame.K_LEFTBRACKET]:
        move.rotateYLeft()
    elif keys[pygame.K_RIGHTBRACKET]:
        move.rotateYRight()
    elif keys[pygame.K_k]:
        move.rotateZForward()
    elif keys[pygame.K_l]:
        move.rotateZBackward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(120)

pygame.quit()
