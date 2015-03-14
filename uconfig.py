
opts_full = \
{
    "gauss-stars" : 1, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 1,  # create a starfield outside of the galaxy(s)


    "spiral-numstars" : 50000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : .15,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 100, # 


    "viewer-auto-rotate" : 0, # move the viewer around the galaxy

    "viewer-x": 0,  # x position of the user 
    "viewer-y": 0,  # y position of the user
    "viewer-angle-x" : 20,
    "viewer-angle-y" : 20,
    "viewer-angle-z" : 20,
    "viewer-distance" : 175
}

opts_realtime = \
{
    "gauss-stars" : 0, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 0,  # create a starfield outside of the galaxy(s)

    "spiral-numstars" : 2000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : .15,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 40, # 

    "viewer-auto-rotate" : 1, # move the viewer around the galaxy

    "viewer-x": 0,  # x position of the viewer 
    "viewer-y": 0,  # y position of the viewer
    "viewer-angle-x" : 0,
    "viewer-angle-y" : 0,
    "viewer-angle-z" : 0,
    "viewer-distance" : 50
}

opts = opts_full
