import sys, math, pygame, random

from pygame.locals import *


def gaussian_decay(A, sigma, x, y):
    """ Return the Z value along a gaussian distribution given x,y 
        coordinates"""
    print(A,x,y)
    g = -((pow(x-16.,2.)/(200.) + (pow(y-16.,2.)/200.)))
    print(g, math.exp(g), A*math.exp(g))
    return A * math.exp(-((pow(x-16.,2.)/(2*pow(sigma,2)) + \
                          (pow(y-16.,2.)/(2*pow(sigma,2))))))
    

class stargfx:

    def __init__(self):
        
        self.stars = []


    def generate_star(self, size, color):
        s = pygame.Surface((64,64))
        s.set_colorkey((0,0,0))
        s.set_alpha(175)

        r = color[0]
        g = color[1]
        b = color[2]

        for i in range(0, 32):
            for j in range(0, 32):
                r_decay = gaussian_decay(r, size, i, j)
                if r_decay < 30:
                    r_decay = 0
                g_decay = gaussian_decay(g, size, i, j)
                if g_decay < 30:
                    g_decay = 0
                b_decay = gaussian_decay(b, size, i, j)
                if b_decay < 30:
                    b_decay = 0
                s.set_at((i,j), (r_decay, g_decay, b_decay))

        return s        

    def generate_row(self, color):
        cache = []
        for i in range (1,8):
            cache.append(self.generate_star(i,color))
        return cache    

    def blit_row(self, stars, row):    
        i = 0
        for star in stars:
            self.screen.blit(star, (i*32,row*32))
            i+=1

    def run_test(self):
        """ Used to visually validate star creation """

        pygame.init()
        self.screen = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()

        self.screen.fill((0,0,0))

        # Red
        stars = self.generate_row((255,0,0))
        self.blit_row(stars,0)
        # yellow
        stars = self.generate_row((255,255,0))
        self.blit_row(stars,1)
        # white
        stars = self.generate_row((255,255,255))
        self.blit_row(stars,2)
        # blue
        stars = self.generate_row((0,0,255))
        self.blit_row(stars,3)
        # white/blue
        stars = self.generate_row((200,200,255))
        self.blit_row(stars,4)
        # white/yellow
        stars = self.generate_row((255,255,200))
        self.blit_row(stars,5)
        # white/red
        stars = self.generate_row((255,200,200))
        self.blit_row(stars,6)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)

            pygame.display.flip()

if __name__ == "__main__":
    stargfx().run_test()
