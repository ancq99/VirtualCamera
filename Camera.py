class Camera:
    ProjectionHeight = 500
    ProjectionWidth = 500
    CameraY = 10.0
    FOV = 200.0

    def __init__(self, height, width, y, fov):
        self.ProjectionHeight = height
        self.ProjectionWidth = width
        self.CameraY = y
        self.FOV = fov

    def getProjectionHeight(self):
        return self.ProjectionHeight

    def getProjectionWidth(self):
        return self.ProjectionWidth

    def getCameraY(self):
        return self.CameraY

    def getFov(self):
        return self.FOV

    def setFov(self, val):
        if self.FOV + val > 0:
            self.FOV += val

