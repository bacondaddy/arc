
import pygame

from star import star3D 

from Vec3d import Vec3d

class axis:

    def __init__(self, pos = Vec3d(0,0,0), show_coords = False):
        self.pos     = pos

        self.x_start = star3D(Vec3d(0,0,0)) 
        self.x_end   = star3D(Vec3d(10,0,0))

        self.y_start = star3D(Vec3d(0,0,0))
        self.y_end   = star3D(Vec3d(0, 10, 0))

        self.z_start = star3D(Vec3d(0,0,0))
        self.z_end   = star3D(Vec3d(0, 0, 10))

        self.show_coords = show_coords

        self.font = pygame.font.SysFont("monospace", 15)

        
    def displayXYZ(self, angleX, angleY, angleZ, viewer, screen):        
        """ Display to screen at rotation defined by XYZ """

        # X axis
        start = self.x_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), 
                              self.pos, 256, viewer)
        end = self.x_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 
                          self.pos, 256, viewer)

        if not start or not end:
            return

        pygame.draw.line(screen, (255,0,0),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y), 3)

        # Y axis
        start = self.y_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), self.pos,
                              256, viewer)
        end = self.y_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 
                          self.pos, 256, viewer)

        pygame.draw.line(screen, (0,255,0),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y), 3)

        # Z axis
        start = self.z_start.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        start = start.project(screen.get_width(), screen.get_height(), 
                              self.pos, 256, viewer)
        end = self.z_end.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
        end = end.project(screen.get_width(), screen.get_height(), 
                          self.pos, 256, viewer)

        pygame.draw.line(screen, (0,0,255),
                         (start.v.x, start.v.y),
                         (end.v.x, end.v.y), 3)

        if self.show_coords:
            label = self.font.render("x : %.2f  y : %.2f z : %.2f"
                                     % (self.pos.x, self.pos.y,
                                         self.pos.z), 1,
                                       (255,255,255))
            screen.blit(label, (start.v.x - 60, start.v.y + (17*1)))
