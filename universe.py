"""

Main driver to test galaxy classes.

TODO:
 - give each galaxy a location in the universe
  
"""
import sys, math, pygame, random

from ellipsoid import ellipsoid

from pygame.locals import *


class Simulation:

    def __init__(self, win_width = 640, win_height = 480):

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        
        self.clock = pygame.time.Clock()

        self.ellipse = ellipsoid(4, 40, 40) 
        self.ellipse.calculate_stars(numstars=1000)

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
                viewer_d += .2 
            elif keystate[K_z]:
                viewer_d -= .2
            elif keystate[K_LEFT]:
                viewer_x -= .2
            elif keystate[K_RIGHT]:
                viewer_x += .2
            elif keystate[K_UP]:
                viewer_y += .2
            elif keystate[K_DOWN]:
                viewer_y -= .2

            self.ellipse.displayXYZ(self.angleX, self.angleY, self.angleZ,
                                    viewer_x, viewer_y, viewer_d, self.screen) 

            # Right now just continuously rotate
            self.angleX += 1
            self.angleY += 1
            self.angleZ += 1
            
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
