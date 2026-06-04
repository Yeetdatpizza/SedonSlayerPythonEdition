class Ruler:
    def __init__(self, angle, position):
        self.angle = angle
        self.position = position

    def getPosition(self):
        return self.position

    def getAngle(self):
        return self.angle

    def setPosition(self, position):
        self.position = position