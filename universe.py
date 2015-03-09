"""

Main driver to test galaxy classes.

TODO:
 - give each galaxy a location in the universe
  
"""
import sys, math, pygame, random

from ellipsoid import ellipsoid
from spiral    import spiral   


from pygame.locals import *


class Simulation:

    def __init__(self, win_width = 640, win_height = 480):

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        
        self.clock = pygame.time.Clock()

        self.spiral = spiral(20, 3 * math.pi, 4) 
        self.spiral.calculate_stars(numstars=8000, starsizedist=[1,1,1,2,3])

        #self.ellipse_disc = ellipsoid(4, 40, 40) 
        #self.ellipse_disc.calculate_stars(numstars=2000)

        #self.ellipse_bulge = ellipsoid(20, 20, 10) 
        #self.ellipse_bulge.calculate_stars(numstars=1000, starsizedist=[1,1,1,2,3])

        self.angleX, self.angleY, self.angleZ = 0, 0, 0
        
    def run(self):
        """ Main Loop """

        viewer_d = 60 
        viewer_x = 0 
        viewer_y = 0 

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,0,0))

            #  Simple key handler to move towards and away from the galazy
            #  using the "a" and "z" keys

            keystate = pygame.key.get_pressed()
            if keystate[K_a]:
                viewer_d += .6 
            elif keystate[K_z]:
                viewer_d -= .6
            elif keystate[K_LEFT]:
                viewer_x -= .6
            elif keystate[K_RIGHT]:
                viewer_x += .6
            elif keystate[K_UP]:
                viewer_y += .6
            elif keystate[K_DOWN]:
                viewer_y -= .6

            self.spiral.displayXYZ(self.angleX, self.angleY, self.angleZ,
                                    viewer_x, viewer_y, viewer_d, self.screen) 
            #self.ellipse_disc.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        viewer_x, viewer_y, viewer_d, self.screen) 
            #self.ellipse_bulge.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        viewer_x, viewer_y, viewer_d, self.screen) 

            # Right now just continuously rotate
            self.angleX += 1
            self.angleY += 1
            self.angleZ += 1
            
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
