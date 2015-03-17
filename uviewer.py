"""

Viewer of universe

Track position, field of view, and direction of viewer
  
"""

from Vec3d import Vec3d

class uviewer:

    def __init__(self, position = Vec3d(0,0,0), direction = Vec3d(1,0,0)):
        self.position  = position
        self.direction = direction
