"""
Contains the Platform class
Has mutator and accesser functions that can be used when needed
THe platform is the ground essentially 
"""

import pygame

class Platform:


    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.top = position[1] - size[1] / 2
        self.bottom = position[1] + size[1] / 2
        self.left = position[0] - size[0] / 2
        self.right = position[0] + size[0] / 2



    def getPosition(self):
        return self.position

    def getSize(self):
        return self.size

    def getBoundingBox(self):
        x = self.getPosition().x -(self.getSize().x / 2)
        y = self.getPosition().y - (self.getSize().y / 2)
        width = self.getSize().x
        height = self.getSize().y
        return [x, y, width, height]

    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def setPosition(self, position):
        self.position.x = position[0]
        self.position.y = position[1]

