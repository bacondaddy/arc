#
# Simple Ellipsoidal galaxy characterized by hieght, width and length.
#
import sys, math, pygame, random

from star import star3D

star_colors = \
  [
  (255, 255, 255), # white
  (255, 255, 255), # white
  (255, 255, 255), # white
  (255, 255, 255), # white
  (199, 189, 50),  # yellow
  (143, 50,  13)  # red
  ]


class ellipsoid:

    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width  = width

        # will be filled once stars are calculated
        self.numstars     = None
        self.starsizedist = None

        self.stars = [] 

    
    def calculate_stars(self, numstars = 1000, starsizedist = [1]):
        """ Calculate random locations for stars within the Ellipsoid """

        self.numstars     = numstars
        self.starsizedist = starsizedist

        for i in range(0, self.numstars):
            
            p = self.generate_random_star() 

            self.stars.append(p)

    # Note that this function should be stateless so that it can be
    # parallelized via standard monte-carlo approaches.  The galaxy class
    # should hold all of the needed parameters and distributions to allow
    # for random generation of a star 

    def generate_random_star(self):

        # choose two random angles
        theta = random.random() * 360
        sigma = random.random() * 360

        a = self.height
        b = self.length
        c = self.width

        x = a * math.cos(theta) * math.sin(sigma) 
        y = b * math.sin(theta) * math.sin(sigma) 
        z = c * math.cos(sigma) 

        starsize = random.choice(self.starsizedist)

        return star3D(x,y,z, color=random.choice(star_colors), size=starsize)

    def displayXYZ(self, angleX, angleY, angleZ, viewer_x, viewer_y, distance,  screen):        
        """ Display to screen at rotation defined by XYZ """
        for star in self.stars:
            # Rotate the point around X axis, then around Y axis, and finally around Z axis.
            s = star.rotateX(angleX).rotateY(angleY).rotateZ(angleZ)
            # Transform the point from 3D to 2D
            p = s.project(screen.get_width(), screen.get_height(), 256,
                          viewer_x, viewer_y, distance)

            # draw to screen 
            pygame.draw.circle(screen, p.color,(int(p.x), int(p.y)), p.size)
