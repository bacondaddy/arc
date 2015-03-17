
import pygame

from star import star3D 

class axis:

    def __init__(self):
        self.x_start = star3D(0,0,0)
        self.x_end   = star3D(10,0,0)

        self.y_start = star3D(0,0,0)
        self.y_end   = star3D(0,10,0)

        self.z_start = star3D(0,0,0)
        self.z_end   = star3D(0,0,10)

        

    def displayXYZ(self, angleX, angleY, angleZ, viewer, screen):        
        """ Display to screen at rotation defined by XYZ """

        # X axis
        start = self.x_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), 256,
                          viewer)
        end = self.x_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 256,
                          viewer)

        if not start or not end:
            return

        pygame.draw.line(screen, (255,0,0),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y))

        # Y axis
        start = self.y_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), 256,
                          viewer)
        end = self.y_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 256,
                          viewer)

        pygame.draw.line(screen, (0,255,0),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y))

        # Z axis
        start = self.z_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), 256,
                          viewer)
        end = self.z_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 256,
                          viewer)

        pygame.draw.line(screen, (0,0,255),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y), 3)
