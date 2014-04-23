#!/usr/bin/env python
#from pylab import *
import getopt
#import os
import sys
import numpy

import trans_coord
from trans_coord import *


DTOR = numpy.pi/180

# Defaults
raC = 0.
decC = 0.
quadrant =1 # in general (field-1)/4 + 1
initfield=1
night = 1
fname = "neo_n1.json"
direction = 1 # go from south to north, middle field is a bit north,
              # the opposite means north to south, middle fields are a
              # bit south
sub_ra = 3 # number of sub_shifts in ra and dec for the sub_cadence
sub_dec= 3 # this one should not be changed

npasses= 4 # number of times the observing stamp is repeated
exptime= 60 # exposure time in seconds
filter='r' # filter selection
dirout='.' # directory where to output files to
verbose=False # whether to print the field centers

# Script that outputs sub_ra x sub_dec field position for optimal coverage using
# DECam@blanco given a cadence center (default 0,0) the cadence starts
# at the south west corner. It moves north and then east, south, east,
# and north.

#get options
args=sys.argv[1:]
try:
    opts, args=getopt.getopt(args, 'ho:d:',['raC=','decC=','initfield=','fname=','night=','direction=','sub_ra=','sub_dec=', 'npasses=', 'exptime=', 'filter=', 'quadrant=', 'dirout=', 'verbose'])

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
    if o in ['--npasses']:
        npasses=int(a)
    if o in ['--exptime']:
        exptime=int(a)
    if o in ['--filter']:
        filter=a
    if o in ['--quadrant']:
        quadrant=int(a)
    if o in ['--dirout']:
        dirout=a
    if o in ['--verbose']:
        verbose=True


fname = dirout+'/'+fname


### DAVID H, added gaps to the step size
#step_ra  = 1.53 #  5[ccd]*4096[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]
#step_dec = 1.84 #  12[ccd]*2048[pix/ccd]*0.27[arcsec/pix]/3600[arcsec/deg]

step_ra  = 1.596 # (5[ccd]*4096[pix/ccd]+4[gaps]*201[pix/gap])*0.27[arcsec/pix]/3600[arcsec/deg]
step_dec = 1.96  # (12[ccd]*2048[pix/ccd]+10[gaps]*153)*0.27[arcsec/pix]/3600[arcsec/deg]

if sub_ra == 3:
    if direction == 1: # north to south
        shifts_dec = numpy.reshape(numpy.array([-step_dec, 0, step_dec]*sub_ra ), (3,-1)) # three different shifts repeated
        shifts_dec[1] += step_dec/2; shifts_dec[1] = shifts_dec[1][::-1] # add a step_dec and revert order for the middle shift
        shifts_dec += numpy.ones(numpy.shape(shifts_dec))*decC # Add zeropoint
    else: # south to north
        shifts_dec = numpy.reshape(numpy.array([step_dec, 0, -step_dec]*sub_ra ), (3,-1)) # three different shifts repeated
        shifts_dec[1] -= step_dec/2; shifts_dec[1] = shifts_dec[1][::-1] # subtract a step_dec and revert order for the middle shift
        shifts_dec += numpy.ones(numpy.shape(shifts_dec))*decC # Add zeropoint

    shifts_ra = numpy.reshape(numpy.array([-step_ra]*3 + [0]*3 + [step_ra]*3 ), (3,-1)) # both start as the same shifts
    fields = numpy.reshape(numpy.array(range(sub_ra*sub_dec)), (3,-1)) + initfield


elif sub_ra == 2:
    if direction == 1: # north to south
        shifts_dec = numpy.reshape(numpy.array([-step_dec/2, step_dec/2]*sub_ra ), (2,-1)) # three different shifts repeated
        shifts_dec[1] += step_dec/2; shifts_dec[1] = shifts_dec[1][::-1] # add a step_dec and revert order for the middle shift
        shifts_dec += numpy.ones(numpy.shape(shifts_dec))*decC # Add zeropoint
    else: # south to north
        shifts_dec = numpy.reshape(numpy.array([step_dec/2, -step_dec/2]*sub_ra ), (2,-1)) # three different shifts repeated
        shifts_dec[1] -= step_dec/2; shifts_dec[1] = shifts_dec[1][::-1] # subtract a step_dec and revert order for the middle shift
        shifts_dec += numpy.ones(numpy.shape(shifts_dec))*decC # Add zeropoint

    shifts_ra = numpy.reshape(numpy.array([-step_ra/2]*2 + [step_ra/2]*2), (2,-1)) # both start as the same shifts
    fields = numpy.reshape(numpy.array(range(sub_ra*sub_dec)), (2,-1)) + initfield

    # 20140423 this should be more clear... only works for 2x2
    nenwswse = 1
    if nenwswse:
        a = fields[1][1]
        fields[1][1]=fields[0,1]
        fields[0,1]=a

shifts_ra /= numpy.cos(shifts_dec*DTOR) # make sure the delta_ra accounts for sky curvature
shifts_ra += numpy.ones(numpy.shape(shifts_ra))*raC # Add zeropoint


lat2dec = numpy.vectorize(lat2dec_s)
lon2ra  = numpy.vectorize(lon2ra_s)

dra = lon2ra(shifts_ra)
ddec = lat2dec(shifts_dec)

# order of coverage is SE -> NW
# change to NE -> SW
#for i in [0,1]:
#    ddec[i] = ddec[i][::-1]
#    dra[i]  = dra[i][::-1]


#dra = dra[::-1].T[::-1]
#ddec= ddec[::-1].T[::-1]

#print dra
#print ddec

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(shifts_ra,shifts_dec,'bo')
#show()
#fig.savefig('test.png')

piece = """ {
  \"comment\": \"%s\",
  \"seqtot\": 1, 
  \"seqnum\": 1, 
  \"expType\": \"object\", 
  \"object\": \"%s\", 
  \"filter\": \"%s\", 
  \"RA\": \"%s\", 
  \"dec\": \"%s\", 
  \"expTime\": %d
 }
"""

# erase night from the names
fobs = open('%s/Q%02d_obsplan.txt'%(dirout,quadrant),'w')
#fobs = open('%s/xN%d_Q%02d_obsplan.txt'%(dirout,night,quadrant),'w')
fobs.write("imname\tRA\tDEC\tEXPTIME\n")
out_l = []
# add 30 sec donut corrector
#out_l.append(piece%("comm", "n%df%d-DONUT"%(night,fields[0,0]), dra[0,0], ddec[0,0], 30))
for k in range(npasses):
    for i in range(sub_dec):
        for j in range(sub_ra):
            # add relevant info, erase Night from file names
            #imname = "N%dQ%dF%dV%d"%(night,quadrant,fields[i,j],k+1)
            imname = "Q%dF%dV%d"%(quadrant,fields[i,j],k+1)
            out_l.append(piece%("Field:%2d , imname:%s "%(fields[i,j],imname), imname, filter, dra[i,j], ddec[i,j], exptime))
            fobs.write("%s\t%s\t%s\t%d\n"%(imname, dra[i,j], ddec[i,j], exptime))

            if verbose and k%npasses==0: # output for xephem visualization
                #print "f%d,f,%s,%f,0,2000"%(fields[i,j], dra[i,j], dec2deg(ddec[i,j]))
                print "F%s,f,%s,%f,0,2000"%(fields[i,j], dra[i,j], dec2deg(ddec[i,j]))
fobs.write("%s\t%s\t%s\t%d\n"%("SLEW_QX_QY", dra[i,j], ddec[i,j], 60))
out = "["+','.join(out_l)+"]" # open and close the script

fobs.close()

f=open(fname,'w'); f.write(out); f.close();


sys.exit()

figure()
plot(shifts_ra.flatten(),shifts_dec.flatten(),'mo-')
xlabel('RA')
ylabel('Dec')
show()


## the whole airmass construct...
#import observer
#obs = observer.Observer('ctio')
#obs.almanac('2010/01/01')

