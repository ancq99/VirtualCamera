#import numpy as np
from numpy import *

class Point:
    vector = None

    def __init__(self):
        self.vector = [0.0, 0.0, 0.0, 1.0]

    def getX(self):
        return self.vector[0]

    def getY(self):
        return self.vector[1]

    def getZ(self):
        return self.vector[2]

    def normalize(self):
        self.vector[0] = self.vector[0] * (1 / self.vector[3])
        self.vector[1] = self.vector[1] * (1 / self.vector[3])
        self.vector[2] = self.vector[2] * (1 / self.vector[3])
        self.vector[3] = 1.0

    def setVector(self, new):
        self.vector = new


class Wall:
    p1 = p2 = p3 = p4 = None
    splitedList = []

    def __init__(self, p):
        self.p1 = p[0]
        self.p2 = p[1]
        self.p3 = p[2]
        self.p4 = p[3]

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getP3(self):
        return self.p3

    def getP4(self):
        return self.p4

    def getPoints(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def getCenter(self):
        vectors = [self.p1.vector, self.p2.vector, self.p3.vector, self.p4.vector]
        x = y = z = 0
        for vec in vectors:
            x += vec[0]
            y += vec[1]
            z += vec[2]

        return x / 4.0, y / 4.0, z / 4.0

    def normalize(self):
        for i in [self.p1, self.p2, self.p3, self.p4]:
            i.normalize()

    def splitWall(self, n):
        x1_split = linspace(self.p1.getX(), self.p2.getX(), n)
        y1_split = linspace(self.p1.getY(), self.p2.getY(), n)
        z1_split = linspace(self.p1.getZ(), self.p2.getZ(), n)

        x2_split = linspace(self.p2.getX(), self.p3.getX(), n)
        y2_split = linspace(self.p2.getY(), self.p3.getY(), n)
        z2_split = linspace(self.p2.getZ(), self.p3.getZ(), n)

        points = {}
        tmp = []

        a = 0

        for i in range(n):
            tmp.append([f"{a} {0}", f"{a} {1}", f"{a + 1} {1}", f"{a + 1} {0}"])
            tmp.append([f"{a} {1}", f"{a} {2}", f"{a + 1} {2}", f"{a + 1} {1}"])
            tmp.append([f"{a} {2}", f"{a} {3}", f"{a + 1} {3}", f"{a + 1} {2}"])
            tmp.append([f"{a} {3}", f"{a} {4}", f"{a + 1} {4}", f"{a + 1} {3}"])
            tmp.append([f"{a} {4}", f"{a} {5}", f"{a + 1} {5}", f"{a + 1} {4}"])
            tmp.append([f"{a} {5}", f"{a} {6}", f"{a + 1} {6}", f"{a + 1} {5}"])
            tmp.append([f"{a} {6}", f"{a} {7}", f"{a + 1} {7}", f"{a + 1} {6}"])
            tmp.append([f"{a} {7}", f"{a} {8}", f"{a + 1} {8}", f"{a + 1} {7}"])
            tmp.append([f"{a} {8}", f"{a} {9}", f"{a + 1} {9}", f"{a + 1} {8}"])
            tmp.append([f"{a} {9}", f"{a} {10}", f"{a + 1} {10}", f"{a + 1} {9}"])
            tmp.append([f"{a} {10}", f"{a} {11}", f"{a + 1} {11}", f"{a + 1} {10}"])
            tmp.append([f"{a} {11}", f"{a} {12}", f"{a + 1} {12}", f"{a + 1} {11}"])
            tmp.append([f"{a} {12}", f"{a} {13}", f"{a + 1} {13}", f"{a + 1} {12}"])
            tmp.append([f"{a} {13}", f"{a} {14}", f"{a + 1} {14}", f"{a + 1} {13}"])
            tmp.append([f"{a} {14}", f"{a} {15}", f"{a + 1} {15}", f"{a + 1} {14}"])
            tmp.append([f"{a} {15}", f"{a} {16}", f"{a + 1} {16}", f"{a + 1} {15}"])
            tmp.append([f"{a} {16}", f"{a} {17}", f"{a + 1} {17}", f"{a + 1} {16}"])
            tmp.append([f"{a} {17}", f"{a} {18}", f"{a + 1} {18}", f"{a + 1} {17}"])
            tmp.append([f"{a} {18}", f"{a} {19}", f"{a + 1} {19}", f"{a + 1} {18}"])
            tmp.append([f"{a} {19}", f"{a} {20}", f"{a + 1} {20}", f"{a + 1} {19}"])
            tmp.append([f"{a} {20}", f"{a} {21}", f"{a + 1} {21}", f"{a + 1} {20}"])
            a += 1

        if array_equal(z1_split, z2_split): # sprawdzamy czy z jest jednakowe dla podziałów
            if all(x2_split[0] == x2_split): # szukamy która współrzędna została podzielona
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x1_split[i], y2_split[j], z1_split[0], 1.0] # tworzymy nowy punkt z obliczonymi wspolrzedymi
                        points[f"{i}{j}"] = p # dodajemy do slownika punktow
            else:
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x2_split[i], y1_split[j], z1_split[0], 1.0]
                        points[f"{i}{j}"] = p

        if array_equal(x1_split, x2_split):
            if all(y1_split[0] == y1_split):
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x1_split[0], y2_split[i], z1_split[j], 1.0]
                        points[f"{i}{j}"] = p
            else:
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x1_split[0], y1_split[i], z2_split[j], 1.0]
                        points[f"{i}{j}"] = p

        if array_equal(y1_split, y2_split):
            if all(x1_split[0] == x1_split):
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x2_split[i], y1_split[0], z1_split[j], 1.0]
                        points[f"{i}{j}"] = p
            else:
                for i in range(n):
                    for j in range(n):
                        p = Point()
                        p.vector = [x1_split[i], y1_split[0], z2_split[j], 1.0]
                        points[f"{i}{j}"] = p

        tmp4 = []
        for i in tmp:
            var = True
            for j in i:
                tmp2 = j.split(" ")
                if int(tmp2[0]) < n-1 and int(tmp2[1]) < n-1:
                    var = False
                    break

            if not var:
                tmp3 = [val.replace(' ', '') for val in i]
                tmp4.append(tmp3)

        for i in tmp4:
            tmp3 = [points[j] for j in i]
            self.splitedList.append(Wall(tmp3))
