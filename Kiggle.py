"""
Contains the Kiggle Enemy class
Has mutator and accesser functions that can be used when needed
"""

class Kiggle:
    def __init__(self, position, image):
        self.position = position
        self.image = image

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getImage(self):
        return self.image
