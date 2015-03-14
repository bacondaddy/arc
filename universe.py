"""

Main driver to test galaxy classes.

TODO:
 - give each galaxy a location in the universe
  
"""

import sys, math, pygame, random

from ellipsoid import ellipsoid
from spiral    import spiral   

import uconfig

from pygame.locals import *

#sizes = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,0,0,0,0,0,0,0]
sizes = uconfig.opts["star-size-dist"]

class Simulation:

    def __init__(self, win_width = 1024, win_height = 768):

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        
        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont("monospace", 15)

        # make a large starfield
        #self.starfield = ellipsoid(60,60,60)
        #self.starfield.calculate_stars(numstars=100, starsizedist=sizes)

        r = uconfig.opts["spiral-diameter"]/2
        self.spiral = spiral(r, 3 * math.pi, 8)
        ns = uconfig.opts["spiral-numstars"]
        self.spiral.calculate_stars(numstars=ns, starsizedist=sizes)

        #self.ellipse_disc = ellipsoid(4, 40, 40) 
        #self.ellipse_disc.calculate_stars(numstars=2000)

        #self.ellipse_bulge = ellipsoid(20, 20, 10) 
        #self.ellipse_bulge.calculate_stars(numstars=1000, starsizedist=[1,1,1,2,3])

        self.angleX = uconfig.opts["viewer-angle-x"]
        self.angleY = uconfig.opts["viewer-angle-y"]
        self.angleZ = uconfig.opts["viewer-angle-z"]

    def display_text(self, string, row, color=(0,255,0)): 
        label = self.font.render(string, 1, color) 
        self.screen.blit(label, (700, 10 + (17*row)))

        
    def run(self):
        """ Main Loop """

        viewer_d = uconfig.opts["viewer-distance"]

        viewer_x = uconfig.opts["viewer-x"] 
        viewer_y = uconfig.opts["viewer-y"] 

        viewer_rotate = uconfig.opts["viewer-auto-rotate"]

        pause = 0 

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,0,0))

            #  Simple key handler to move towards and away from the galazy
            #  using the "a" and "z" keys

            keystate = pygame.key.get_pressed()
            if keystate[K_e]:
                viewer_d += .6 
            elif keystate[K_r]:
                viewer_d -= .6
            elif keystate[K_q]:
                self.angleX +=1 
            elif keystate[K_w]:
                self.angleX -=1 
            elif keystate[K_a]:
                self.angleY +=1 
            elif keystate[K_s]:
                self.angleY -=1 
            elif keystate[K_z]:
                self.angleZ +=1 
            elif keystate[K_x]:
                self.angleZ -=1 
            elif keystate[K_LEFT]:
                viewer_x -= .6
            elif keystate[K_RIGHT]:
                viewer_x += .6
            elif keystate[K_UP]:
                viewer_y += .6
            elif keystate[K_DOWN]:
                viewer_y -= .6
            elif keystate[K_p]:
                pause = pause ^ 1 # toggle pause


            self.spiral.displayXYZ(self.angleX, self.angleY, self.angleZ,
                                    viewer_x, viewer_y, viewer_d, self.screen) 
            #self.starfield.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        viewer_x, viewer_y, viewer_d, self.screen) 
            #self.ellipse_disc.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        viewer_x, viewer_y, viewer_d, self.screen) 
            #self.ellipse_bulge.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        viewer_x, viewer_y, viewer_d, self.screen) 

            self.display_text("viewer-x : %d" % viewer_x, row=0)    
            self.display_text("viewer-y : %d" % viewer_y, row=1)    
            self.display_text("viewer-angle-x : %d" % self.angleX, row=2)    
            self.display_text("viewer-angle-y : %d" % self.angleY, row=3)    
            self.display_text("viewer-angle-z : %d" % self.angleZ, row=4)    

            if viewer_rotate and not pause:
                self.angleX += 1
                self.angleY += 1
                self.angleZ += 1
            
            pygame.display.flip()

if __name__ == "__main__":

    Simulation().run()
