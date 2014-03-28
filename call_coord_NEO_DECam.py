#!/usr/bin/env python
from pylab import *
import getopt
import os
import sys
import numpy

from trans_coord import *

DTOR = numpy.pi/180


# Defaults
raC = 0.
decC = 0.
initfield=1
night = 1
fname = "neo_n1.json"
direction = 1 # go from south to north, middle field is a bit north,
              # the opposite means north to south, middle fields are a
              # bit south
sub_ra = 3 # number of sub_shifts in ra and dec for the sub_cadence
sub_dec= 3 # this one should not be changed

# Script that outputs sub_ra x sub_dec field position for optimal coverage using
# DECam@blanco given a cadence center (default 0,0) the cadence starts
# at the south west corner. It moves north and then east, south, east,
# and north.

#get options
args=sys.argv[1:]
try:
    opts, args=getopt.getopt(args, 'ho:d:',['raC=','decC=','initfield=','fname=','night=','direction=','sub_ra=','sub_dec='])
except:
    sys.exit(2)
for o, a in opts:
    if o in ['--raC']:
        try:
            raC=ra2deg(a)
        except:
            raC=float(a)
    if o in ['--decC']:
        try:
            decC=dec2deg(a)
        except:
            decC=float(a)
    if o in ['--initfield']:
        initfield=int(a)
    if o in ['--night']:
        night=int(a)
    if o in ['--fname']:
        fname=a
    if o in ['--direction']:
        if a == 'north':
            direction = 1
        elif a == 'south':
            direction = -1
        else:
            direction = 1
    if o in ['--sub_ra']: # number of ra shifts
        sub_ra=int(a)
    if o in ['--sub_dec']: # number of dec shifts... right now has to be 3.
        sub_dec=int(a)

print 'night',night

### CHECK THESE NUMBERS
step_dec = 1.84 #  12[ccd]*2048[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]
step_ra  = 1.53 #  5[ccd]*4096[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]

ras = (array(range(5)) - 4./2)*step_ra*2 # remember these will be 2x2 chuncks
ras = reshape(array(list(ras) *5), (5,-1))

decs = (array(range(5)) - 4./2)*step_dec*2 # remember these will be 2x2 chuncks
decs = reshape(array(list(decs) *5), (5,-1))
decs = decs.T # flip so that we don't get just the diagonal
decs  += numpy.ones(numpy.shape(decs))*decC# Add zeropoint

ras /= numpy.cos(decs*DTOR) # make sure the delta_ra accounts for sky curvature
ras += numpy.ones(numpy.shape(ras))*raC # Add zeropoint

print ras
print decs

#plot(ras,decs,'bo')
#show()

q = 0
for i in range(5):
    for j in range(5):
        initfield = q*4 + 1
        q = q+1
        util = 'python point_coord_NEO_DECam.py --raC %f --decC %f --initfield %d --night %d --fname neo_n%dq%d.json --direction north --sub_ra 2 --sub_dec 2'%(ras[i][j], decs[i][j], initfield, night, night,q)
        os.system(util)




