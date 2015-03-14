
opts = \
{
    "gauss-stars" : 1, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 1,  # create a starfield outside of the galaxy(s)
    "spiral-numstars" : 3000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : .10, # entropy to throw at spiral galaxy 
    "viewer-distance" : 100
}
