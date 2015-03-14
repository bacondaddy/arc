
opts = \
{
    "gauss-stars" : 1, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 1,  # create a starfield outside of the galaxy(s)
    "spiral-numstars" : 15000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : .15,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 100, # 
    "viewer-x": 0,  # x position of the user 
    "viewer-y": 0,  # y position of the user
    "viewer-angle-x" : 90,
    "viewer-angle-y" : 90,
    "viewer-angle-z" : 90,
    "viewer-distance" : 5
}
