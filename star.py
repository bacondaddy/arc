#  Sun Mar 01 18:30:17 PST 2015  
#
#  Base star class which is the basic unit of composition for the Galaxy.  In #  the future should pull out the geomatric transformation functions into a
#  base class, but this'll work for now.
#

import sys, math, pygame, random

from Vec3d import Vec3d

class star3D:

    def __init__(self, x = 0, y = 0, z = 0, color = (255,255,255), size=1 ):
        self.v = Vec3d(float(x), float(y), float(z))
        self.color = color
        self.size  = size

    def rotateX(self, angle):
        """ Rotate the star around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.v.y * cosa - self.v.z * sina
        z = self.v.y * sina + self.v.z * cosa
        return star3D(self.v.x, y, z, self.color, self.size)
 
    def rotateY(self, angle):
        """ Rotate the star around the Y axis by the given angle in degrees. """
        rad = math.radians(angle)
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.v.z * cosa - self.v.x * sina
        x = self.v.z * sina + self.v.x * cosa
        return star3D(x, self.v.y, z, self.color, self.size)
 
    def rotateZ(self, angle):
        """ Rotate the star around the Z axis by the given angle in degrees. """
        rad = math.radians(angle)
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.v.x * cosa - self.v.y * sina
        y = self.v.x * sina + self.v.y * cosa
        return star3D(x, y, self.v.z, self.color, self.size)
 
    def project(self, win_width, win_height, fov, viewer):
        """ Transforms this 3D point to 2D using a perspective projection. """

        # The following chunc of code determines whether the star is
        # outside of the viewers scope by simplistically determining if
        # it is behind the viewer, in which case, it doesn't project the
        # star

        # Note the the viewer is viewer_d along the z axes and looking
        # back (0,0,-1) therefore we use S+V to find the distance
        dist = self.v - viewer.position # distance from star to viewer

        if dist.z > 0:
            return None

        if (viewer.position.z - self.v.z) == 0:
            factor = 0
        else:    
            factor = fov / (viewer.position.z - self.v.z)
        x = (self.v.x+viewer.position.x) * factor + win_width / 2
        y = -(self.v.y+viewer.position.y) * factor + win_height / 2
        return star3D(x, y, 0, self.color, self.size)

