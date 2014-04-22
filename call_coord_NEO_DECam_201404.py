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
direction = 'north' # go from south to north, middle field is a bit north,
              # the opposite means north to south, middle fields are a
              # bit south
sub_ra = 2 # number of sub_shifts in ra and dec for the sub_cadence
sub_dec= 2 # this one should not be changed

len_ra = 2 # number of shifts for each sub_field in ra
len_dec= 2 # number of shifts for each sub_field in dec

exptime=40 # exptime in seconds
filter='r' # filter selection
npasses= 5 # number of times the observing stamp is repeated
dirout='.' # directory where to output files to

# Script that outputs sub_ra x sub_dec field position for optimal coverage using
# DECam@blanco given a cadence center (default 0,0) the cadence starts
# at the south west corner. It moves north and then east, south, east,
# and north.

#get options
args=sys.argv[1:]
try:
    opts, args=getopt.getopt(args, 'ho:d:',['raC=','decC=','initfield=','fname=','night=','direction=','sub_ra=','sub_dec=','len_ra=','len_dec=','exptime=','filter=','npasses=','utcinit=','dirout='])
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
        direction = a
#        if a == 'north':
#            direction = 1
#        elif a == 'south':
#            direction = -1
#        else:
#            direction = 1
    if o in ['--sub_ra']: # number of ra shifts
        sub_ra=int(a)
    if o in ['--sub_dec']: # number of dec shifts... right now has to be 3.
        sub_dec=int(a)

    if o in ['--len_ra']: # number of ra subshifts
        len_ra=int(a)
    if o in ['--len_dec']: # number of dec subshifts
        len_dec=int(a)
    if o in ['--exptime']:
        exptime=int(a)
    if o in ['--filter']:
        filter=a
    if o in ['--npasses']:
        npasses=int(a)
    if o in ['--utcinit']:
        utcinit=a
    if o in ['--dirout']:
        dirout=a

print '# night',night

### CHECK THESE NUMBERS
#step_dec = 1.84 #  12[ccd]*2048[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]
#step_ra  = 1.53 #  5[ccd]*4096[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]
step_ra  = 1.596 # (5[ccd]*4096[pix/ccd]+4[gaps]*201[pix/gap])*0.27[arcsec/pix]/3600[arcsec/deg]
step_dec = 1.96  # (12[ccd]*2048[pix/ccd]+10[gaps]*153)*0.27[arcsec/pix]/3600[arcsec/deg]

ras = (array(range(len_ra)) - (len_ra-1)/2.)*step_ra*2 # remember these will be 2x2 chuncks
ras = reshape(array(list(ras) *len_ra), (len_ra,-1))

decs = (array(range(len_dec))  - (len_dec-1)/2.)*step_dec*2 # remember these will be 2x2 chuncks
decs = reshape(array(list(decs) *len_dec), (len_dec,-1))
decs = decs.T # flip so that we don't get just the diagonal
decs  += numpy.ones(numpy.shape(decs))*decC# Add zeropoint

## FIX THIS
#ras = (array(range(len_ra)) - len_ra/4.)*step_ra*2 # remember these will be 2x2 chuncks
#ras = reshape(array(list(ras) *len_dec), (len_ra,-1))
#decs = (array(range(len_dec))  - len_dec/4.)*step_dec*2 # remember these will be 2x2 chuncks
#decs = reshape(array(list(decs) *len_dec), (len_ra,-1))
#decs = decs.T # flip so that we don't get just the diagonal
#decs  += numpy.ones(numpy.shape(decs))*decC# Add zeropoint



# Order of quadrants is SE -> NW
# Try to change quadrants to get NE -> SW
ras  = ras[::-1].T
decs = decs[::-1].T


ras /= numpy.cos(decs*DTOR) # make sure the delta_ra accounts for sky curvature
ras += numpy.ones(numpy.shape(ras))*raC # Add zeropoint


#print ras
#print decs


#plot(ras,decs,'bo')
#show()



chunksra = 2
chunksdec= 2

q = 0
for i in range(len_ra):
    for j in range(len_dec):
        #initfield = q*sub_ra*sub_dec + 1
        initfield = 1 # keep info in Q and F, Q2F1 (instead of Q2F5)
        q = q+1
        util = 'python point_coord_NEO_DECam.py --raC %f --decC %f --initfield %d --quadrant %d --fname neo_q%02d.json --direction %s --sub_ra 2 --sub_dec 2 --exptime %d --filter %s --npasses %d --dirout %s'%(ras[i][j], decs[i][j], initfield, q, q, direction, exptime, filter, npasses, dirout)
        os.system(util)
        print "Q%d,f,%s,%.3f,0,2000"%(q,lon2ra_s(ras[i,j]), decs[i,j])
        #print lon2ra_s(ras[i,j]), decs[i,j]
os.system('')

