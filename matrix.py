from numpy import *


class Matrix:
    matrix = None
    camera = None

    def __init__(self, camera=None):
        self.matrix = eye(4)
        self.camera = camera

    def set(self, row, col, value):
        self.matrix[row][col] = value

    def multiply(self, matrix2):
        newMatrix = matmul(self.matrix, matrix2)
        self.matrix = newMatrix

    def reset(self):
        self.matrix = eye(4)

    def XRotation(self, alpha):
        matrix = eye(4)
        c = self.camera.getCameraY()

        matrix[1][1] = cos(alpha)
        matrix[1][2] = -sin(alpha)
        matrix[2][2] = cos(alpha)
        matrix[2][1] = sin(alpha)

        matrix[1][3] = c * (cos(alpha) - 1)
        matrix[2][3] = c * sin(alpha)

        return matrix

    def YRotation(self, alpha):
        matrix = eye(4)

        matrix[0][0] = cos(alpha)
        matrix[0][2] = sin(alpha)
        matrix[2][2] = cos(alpha)
        matrix[2][0] = -sin(alpha)

        return matrix

    def ZRotation(self, alpha):
        matrix = eye(4)
        c = self.camera.getCameraY()

        matrix[0][0] = cos(alpha)
        matrix[0][1] = -sin(alpha)
        matrix[1][1] = cos(alpha)
        matrix[1][0] = sin(alpha)

        matrix[0][3] = (-1 * sin(alpha) * c)
        matrix[1][3] = (cos(alpha) - 1) * c

        return matrix
