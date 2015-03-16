
import argparse

opts_full = \
{
    "gauss-stars" : 1, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 1,  # create a starfield outside of the galaxy(s)

    "star-size-dist" : [0,0,0,0,0,0,1,1,1,2],

    "spiral-numstars" : 10000, # number of stars used to make up the
                              # spiral galaxy
    "spiral-fuzz" : .15,  # entropy to throw at spiral galaxy 
    "spiral-diameter" : 500, # 


    "viewer-auto-rotate" : 0, # move the viewer around the galaxy

    "viewer-x": 0,  # x position of the user 
    "viewer-y": 0,  # y position of the user
    "viewer-angle-x" : 0,
    "viewer-angle-y" : 0,
    "viewer-angle-z" : 0,
    "viewer-distance" : 800
}

opts_realtime = \
{
    "gauss-stars" : 0, # use gaussian attenuation for stars
                       # this has a major performance impact so
                       # not good for real time viewing with high
                       # numbers of stars
    "star-field" : 0,  # create a starfield outside of the galaxy(s)

    "star-size-dist" : [0,0,0,0,0,0,1,1,1,2],

    "spiral-numstars" : 4000, # number of stars used to make up the
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

cla_parser = argparse.ArgumentParser(description='Galaxy creation and viewing')
cla_parser.add_argument('-r','--realtime', action='store_true', help='configurations to allow for real time viewing')

args = cla_parser.parse_args()

if args.realtime:
    opts = opts_realtime
else:
    opts = opts_full
