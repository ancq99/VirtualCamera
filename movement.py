from matrix import Matrix


class movement:
    scene = camera = None

    translationStep, rotationStep, zoomStep = 7, 0.01, 2.5

    translationVector = [0.0, 0.0, 0.0]
    translationMatrix = Matrix()
    rotationMatrix = Matrix()

    rotationXUp = rotationXDown = rotationYLeft = rotationYRight = rotationZForward = rotationZBackward = None

    def __init__(self, scene, camera):
        self.scene = scene
        self.camera = camera

        self.rotationXUp = Matrix(camera).XRotation(-self.rotationStep)
        self.rotationXDown = Matrix(camera).XRotation(self.rotationStep)
        self.rotationYLeft = Matrix(camera).YRotation(-self.rotationStep)
        self.rotationYRight = Matrix(camera).YRotation(self.rotationStep)
        self.rotationZForward = Matrix(camera).ZRotation(-self.rotationStep)
        self.rotationZBackward = Matrix(camera).ZRotation(self.rotationStep)

    def moveRight(self):
        self.translationVector[0] -= self.translationStep
        self.updateView()

    def moveLeft(self):
        self.translationVector[0] += self.translationStep
        self.updateView()

    def moveForward(self):
        self.translationVector[1] -= self.translationStep
        self.updateView()

    def moveBackward(self):
        self.translationVector[1] += self.translationStep
        self.updateView()

    def moveUp(self):
        self.translationVector[2] -= self.translationStep
        self.updateView()

    def moveDown(self):
        self.translationVector[2] += self.translationStep
        self.updateView()

    def zoomIn(self):
        self.camera.setFov(self.zoomStep)
        self.updateView()

    def zoomOut(self):
        self.camera.setFov((-1) * self.zoomStep)
        self.updateView()

    def rotateXUp(self):
        self.rotationMatrix.multiply(self.rotationXUp)
        self.updateView()

    def rotateXDown(self):
        self.rotationMatrix.multiply(self.rotationXDown)
        self.updateView()

    def rotateYLeft(self):
        self.rotationMatrix.multiply(self.rotationYLeft)
        self.updateView()

    def rotateYRight(self):
        self.rotationMatrix.multiply(self.rotationYRight)
        self.updateView()

    def rotateZForward(self):
        self.rotationMatrix.multiply(self.rotationZForward)
        self.updateView()

    def rotateZBackward(self):
        self.rotationMatrix.multiply(self.rotationZBackward)
        self.updateView()

    def updateView(self):

        for i, val in enumerate(self.translationVector):
            self.translationMatrix.set(i, 3, val)

        self.scene.multiply(self.translationMatrix.matrix, self.rotationMatrix.matrix)

        self.scene.project()

        self.translationMatrix.reset()
        self.rotationMatrix.reset()

        self.translationVector = [0.0, 0.0, 0.0]
