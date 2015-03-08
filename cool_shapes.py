
# Looks like a snail shell
    def generate_random_star(self):

        t = self.alpha * random.random()
        
        s = sign(t)
        t = abs(t)

        r = self.r * math.sqrt(t)
        x1 = s * r * math.cos(t)
        y1 = s * r * math.sin(t)
        # z1 = zeros(N,1);

        # create a sphere
        theta = random.random() * 360.
        phi   = random.random() * 360.

        rho = r
        x0 = rho * math.cos(theta) * math.sin(phi)
        y0 = rho * math.sin(theta) * math.sin(phi)
        z0 = rho * math.cos(phi);

        # combine spiral and sphere to create spiral galaxy
        # with dense cloud at center
        alpha   = (1. + math.cos(math.pi*r/(r)))/3.;
        alpha_z = (1. + math.cos(math.pi*r/(r)))/6.;

        x = alpha * x0 + (1.-alpha) * x1;
        y = alpha * y0 + (1.-alpha) * y1;
        z = alpha_z * z0;

        return star3D(x1 + x0,y1 + y0,z0)

