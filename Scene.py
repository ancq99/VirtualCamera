from pygame.display import update
from numpy import *
from numpy.linalg import multi_dot
from pygame.gfxdraw import polygon, filled_polygon
import data


class Scene:
    camera = walls = screen = None
    vertexes = []
    ratio = 2
    updateRatio = 0
    color_final = []

    def __init__(self, walls, camera, screen, ratio):
        self.walls = walls
        self.camera = camera
        self.screen = screen
        self.ratio = (ratio + 1)

        self.updateRatio = (self.ratio - 2) ** 2

        color_fill = [[(255, 120, 120)], [(120, 255, 120)], [(120, 120, 255)], [(255, 255, 120)], [(120, 255, 255)], [(255, 120, 255)]]
        color_fill_ratio = [element * self.updateRatio for element in color_fill]

        self.color_final = []

        for i in color_fill_ratio:
            for j in i:
                self.color_final.append(j)

    def multiply(self, translationMatrix, rotationMatrix):
        for wall in self.walls:
            p1, p2, p3, p4 = wall.getPoints()

            tmp = data.Point()
            tmp.vector = translationMatrix @ rotationMatrix @ p1.vector
            wall.p1 = tmp

            tmp = data.Point()
            tmp.vector = translationMatrix @ rotationMatrix @ p2.vector
            wall.p2 = tmp

            tmp = data.Point()
            tmp.vector = translationMatrix @ rotationMatrix @ p3.vector
            wall.p3 = tmp

            tmp = data.Point()
            tmp.vector = translationMatrix @ rotationMatrix @ p4.vector
            wall.p4 = tmp

            #wall.normalize()

    def project(self):
        color_border = (0, 0, 0)
        painters = []

        color = 0
        segment = 0

        for wall in self.walls:
            x1, y1 = self.projectPoint(wall.getP1())
            x2, y2 = self.projectPoint(wall.getP2())
            x3, y3 = self.projectPoint(wall.getP3())
            x4, y4 = self.projectPoint(wall.getP4())

            self.vertexes = ((x1, y1), (x2, y2), (x3, y3), (x4, y4))

            x, y, z = wall.getCenter()
            distance = sqrt(x ** 2 + y ** 2 + z ** 2)

            painters.append((color, distance, self.vertexes, self.color_final[color]))
            color += 1
            segment += 1

            if color == (6*self.updateRatio):
                color = 0

        self.screen.fill((150, 150, 150))

        sortedPainters = sorted(painters, key=lambda x: x[1], reverse=True)
        for idx, dist, vertex, color in sortedPainters:
            filled_polygon(self.screen, vertex, color)
            polygon(self.screen, vertex, color_border)

        update()

    def projectPoint(self, point):
        x = point.getX()
        y = point.getY()
        z = point.getZ()

        try:
            k = self.camera.getFov() / (float(y) - self.camera.getCameraY())
        except ZeroDivisionError:
            k = self.camera.getFov() / 0.000001

        x1 = int(k * float(x) + self.camera.getProjectionWidth() / 2)
        z1 = int(self.camera.getProjectionHeight() / 2 - k * float(z))

        return x1, z1
