"""

Main driver to test galaxy classes.

TODO:
 - give each galaxy a location in the universe
  
"""

import sys, math, pygame, random

import uviewer

from ellipsoid import ellipsoid
from spiral    import spiral   
from Vec3d     import Vec3d

import uconfig

from pygame.locals import *

#sizes = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,0,0,0,0,0,0,0]
sizes = uconfig.opts["star-size-dist"]

class Simulation:

    def __init__(self, win_width = 1024, win_height = 768):

        pygame.init()

        # Pygame init
        self.screen = pygame.display.set_mode((win_width, win_height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 15)

        # make a large starfield
        #self.starfield = ellipsoid(60,60,60)
        #self.starfield.calculate_stars(numstars=100, starsizedist=sizes)

        self.viewer = uviewer.uviewer(screen_width=win_width,
                                      screen_height=win_height) 

        r = uconfig.opts["spiral-diameter"]/2
        self.spiral  = spiral(Vec3d(0,70,0), r, 3 * math.pi, 8)
        self.spiral2 = spiral(Vec3d(-70,-70,0), 1.3*r, 3 * math.pi, 4)
        ns = uconfig.opts["spiral-numstars"]
        self.spiral. calculate_stars(numstars=ns, starsizedist=sizes)
        self.spiral2.calculate_stars(numstars=ns, starsizedist=sizes)

        #self.ellipse_disc = ellipsoid(4, 40, 40) 
        #self.ellipse_disc.calculate_stars(numstars=2000)

        #self.ellipse_bulge = ellipsoid(20, 20, 10) 
        #self.ellipse_bulge.calculate_stars(numstars=1000, starsizedist=[1,1,1,2,3])

        self.angleX = uconfig.opts["obj-angle-x"]
        self.angleY = uconfig.opts["obj-angle-y"]
        self.angleZ = uconfig.opts["obj-angle-z"]

    def display_text(self, string, row, color=(0,255,0)): 
        label = self.font.render(string, 1, color) 
        self.screen.blit(label, (700, 10 + (17*row)))

        
    def run(self):
        """ Main Loop """

        self.viewer.position.x = uconfig.opts["viewer-x"] 
        self.viewer.position.y = uconfig.opts["viewer-y"] 
        self.viewer.position.z = uconfig.opts["viewer-z"]

        self.viewer.direction  = uconfig.opts["viewer-dir"]

        viewer_rotate = uconfig.opts["obj-auto-rotate"]

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
                self.viewer.position.z += .6 
            elif keystate[K_r]:
                self.viewer.position.z -= .6
            if keystate[K_t]:
                self.viewer.direction.x += .2 
            elif keystate[K_y]:
                self.viewer.direction.x -= .2
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
                self.viewer.position.x -= .6
            elif keystate[K_RIGHT]:
                self.viewer.position.x += .6
            elif keystate[K_UP]:
                self.viewer.position.y += .6
            elif keystate[K_DOWN]:
                self.viewer.position.y -= .6
            elif keystate[K_p]:
                pause = pause ^ 1 # toggle pause


            self.spiral.displayXYZ(self.angleX, self.angleY, self.angleZ,
                                    self.viewer, self.screen) 
            self.spiral2.displayXYZ(self.angleX, self.angleY, self.angleZ,
                                    self.viewer, self.screen) 
            self.viewer.displayXYZ(0, 0, 0, self.viewer, self.screen) 
                                    
            #self.starfield.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        self.viewer.position.x, self.viewer.position.y, self.viewer.position.z, self.screen) 
            #self.ellipse_disc.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        self.viewer.position.x, self.viewer.position.y, self.viewer.position.z, self.screen) 
            #self.ellipse_bulge.displayXYZ(self.angleX, self.angleY, self.angleZ,
            #                        self.viewer.position.x, self.viewer.position.y, self.viewer.position.z, self.screen) 

            self.display_text("viewer-x : %d" % self.viewer.position.x, row=0)    
            self.display_text("viewer-y : %d" % self.viewer.position.y, row=1)    
            self.display_text("viewer-z : %d" % self.viewer.position.z, row=2)    

            self.display_text("obj-angle-x : %d" % self.angleX, row=3)    
            self.display_text("obj-angle-y : %d" % self.angleY, row=4)    
            self.display_text("obj-angle-z : %d" % self.angleZ, row=5)    

            self.display_text("viewer-dir-x : %f" % self.viewer.direction.x, row=6)    

            if viewer_rotate and not pause:
                self.angleX += 1
                self.angleY += 1
                self.angleZ += 1
            
            pygame.display.flip()

if __name__ == "__main__":

    Simulation().run()
