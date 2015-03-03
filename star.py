#  Sun Mar 01 18:30:17 PST 2015  
#
#  Base star class which is the basic unit of composition for the Galaxy.  In
#  the future should pull out the geomatric transformation functions into a
#  base class, but this'll work for now.
#

import sys, math, pygame, random


class star3D:

    def __init__(self, x = 0, y = 0, z = 0, color = (255,255,255), size=1 ):
        self.x, self.y, self.z = float(x), float(y), float(z)
        self.color = color
        self.size  = size

    def rotateX(self, angle):
        """ Rotate the star around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return star3D(self.x, y, z, self.color)
 
    def rotateY(self, angle):
        """ Rotate the star around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return star3D(x, self.y, z, self.color)
 
    def rotateZ(self, angle):
        """ Rotate the star around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return star3D(x, y, self.z, self.color)
 
    def project(self, win_width, win_height, fov, viewer_x, viewer_y, viewer_d):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_d + self.z)
        x = (self.x+viewer_x) * factor + win_width / 2
        y = -(self.y+viewer_y) * factor + win_height / 2
        return star3D(x, y, 1, self.color)


