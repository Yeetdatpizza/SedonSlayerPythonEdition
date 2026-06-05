"""
This is pretty much just a positioning system for the ruler,
Containing it in a class makes it more manageable
Much like them platform
"""

class Ruler:
    def __init__(self, angle, position, timeAlive):
        self.angle = angle
        self.position = position
        self.timeAlive = timeAlive

    def getPosition(self):
        return self.position

    def getAngle(self):
        return self.angle

    def setPosition(self, position):
        self.position = position

    def wither(self):
        self.timeAlive -= 1

    def getTimeAlive(self):
        return self.timeAlive
