"""

Viewer of universe

Track position, field of view, and direction of viewer
  
"""

from Vec3d import Vec3d

from axis      import axis

class uviewer:

    def __init__(self,screen_width, screen_height, position = Vec3d(0,0,0),
                 direction = Vec3d(1,0,0)):
        self.position  = position
        self.direction = direction



    def displayXYZ(self, angleX, angleY, angleZ, viewer, screen):        
        # Create a reference coordinate axis for the universe based on the
        # viewers position.  
        self.universe_axis = axis(Vec3d( (-self.position.x)-140,
                                         (-self.position.y)+120,
                                         (-self.position.z)+100),
                                          show_coords = True);

        self.universe_axis.displayXYZ(angleX, angleY, angleZ, self, screen)
