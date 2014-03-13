import numpy as np
#import orbfit
# Transforms typical coordinate format (string to deg for example)
# and provide wrappers to the orbfit.transforms package


# Change the format of the ticks
def lat2str(deg):
    min = 60 * (deg - np.floor(deg))
    deg = np.floor(deg)
    dir = 'N'
    if deg < 0:
        if min != 0.0:
            deg += 1.0
            min -= 60.0
        dir = 'S'
    return (u"%d\N{DEGREE SIGN} %g' %s") % (np.abs(deg),np.abs(min),dir)

def lon2str(deg):
    min = 60 * (deg - np.floor(deg))
    deg = np.floor(deg)
    dir = 'E'
    if deg < 0:
        if min != 0.0:
            deg += 1.0
            min -= 60.0
        dir = 'W'
    return (u"%d\N{DEGREE SIGN} %g' %s") % (np.abs(deg),np.abs(min),dir)

# Change to ra/dec
def lat2dec(deg):
    min = 60 * (deg - np.floor(deg))
    deg = np.floor(deg)
    signo = ''
    if deg < 0:
        if min != 0.0:
            deg += 1.0
            min -= 60.0
        signo = '-'
    return (u"%s%d\N{DEGREE SIGN} %g'") % (signo,np.abs(deg),np.abs(min))

def lon2ra(deg):
    # Since I want to have the 
    if deg < 0:
        deg += 360.
    deg *= 24./360.
    min = 60 * (deg - np.floor(deg))
    deg = np.floor(deg)
    return (u"%dh %gm") % (np.abs(deg),np.abs(min))

# Change to ra/dec in longer format w/ seconds
def lat2dec_s(deg,sdec=None):
    min = 60 * (deg - np.floor(deg))
    sec = 60 * (min - np.floor(min))
    deg = np.floor(deg)
    signo = ''
    if deg < 0:
        if min != 0.0:
            deg += 1.0
            min -= 60.0
        sec  = 60 * (min - np.floor(min))
        min = np.floor(min)
        signo = '-'
    if sdec is not None:
        fstring = u"%s%d.%df"%("%s%d:%d:%0",sdec+3,sdec)
        print fstring
        return (fstring) % (signo,np.abs(deg),np.abs(min),np.abs(sec))
    return (u"%s%02d:%02d:%02d") % (signo,np.abs(deg),np.abs(min),np.abs(sec))


def lon2ra_s(deg,sdec=None):
    if deg < 0:
        deg += 360.
    deg *= 24./360.
    min = 60 * (deg - np.floor(deg))
    sec = 60 * (min - np.floor(min))
    deg = np.floor(deg)
    min = np.floor(min)
    if sdec is not None:
        fstring = u"%s%d%s%df"%("%d:%02d:%0",2,"d.%.",sdec)
        print fstring
        return (fstring) % (np.abs(deg),np.abs(min),np.abs(sec),sec-np.abs(sec))
    return (u"%02d:%02d:%02d") % (np.abs(deg),np.abs(min),np.abs(sec))

### Change ra/dec to deg
#def dec2deg(dec):
#    h, m, s = dec.split(':'); h=float(h); m=float(m); s=float(s);
#    signo = 1.
#    if h<0: signo = -1.
#    #signo = int(h/abs(h));
#    h=abs(h);
#    deg  = h + m/60. + s/3600.
#    return deg*signo
#
#def ra2deg(ra):
#    h, m, s = ra.split(':'); h=float(h); m=float(m); s=float(s);
#    signo = 1.
#    if h<0: signo = -1.
#    #signo = int(h/abs(h));
#    h=abs(h);
#    deg  = h*15. + m/4. + s/240.
#    return deg*signo

# Change ra/dec to deg
def dec2deg(dec):
    h, m, s = dec.split(':');
    signo = 1.
    if h[0]=='-': signo = -1.
    h=abs(float(h)); m=float(m); s=float(s);
    deg  = h + m/60. + s/3600.
    return deg*signo

def ra2deg(ra):
    h, m, s = ra.split(':');
    signo = 1.
    if h[0]=='-': signo = -1.
    h=abs(float(h)); m=float(m); s=float(s);
    deg  = h*15. + m/4. + s/240.
    return deg*signo     
                    


### ORBFIT coordinate transformations... remember that this is not a
### class (should be), hence for xyz definition of coordinate system
### should be passed to all those methods
###
#
#def eq2ec(ra, dec):
#    lat,lon=orbfit.eq_to_ec(ra*orbfit.DTOR, dec*orbfit.DTOR,None)
#    return lat/orbfit.DTOR, lon/orbfit.DTOR
#
#def ec2eq(lat, lon):
#    ra,dec=orbfit.ec_to_eq(lat*orbfit.DTOR, lon*orbfit.DTOR,None)
#    return ra/orbfit.DTOR, dec/orbfit.DTOR
#
#def abg_to_aei(a,b,g,adot,bdot,gdot, lat0,lon0,xBary,yBary,zBary,jd0): # transform a pbasis to an orbital set
#    orbfit.cvar.lat0,orbfit.cvar.lon0,orbfit.cvar.xBary,orbfit.cvar.yBary,orbfit.cvar.zBary,orbfit.cvar.jd0 = p[lat0*orbfit.DTOR,lon0*orbfit.DTOR,xBary,yBary,zBary,jd0]
#    pb=orbfit.PBASIS()
#    pb.a=p['a'];pb.adot=p['adot'];pb.b=p['b'];pb.bdot=p['bdot'];pb.g=p['g'];pb.gdot=p['gdot'];
#
#    xv=orbfit.XVBASIS()
#    orbfit.pbasis_to_bary(pb,xv,None)
#    orb=orbfit.ORBIT()
#    orbfit.orbitElements(xv,orb)
#    dd=(orbfit.cvar.xBary**2+orbfit.cvar.yBary**2+(orbfit.cvar.zBary-1/pb.g)**2)**.5
#    return orb.a, orb.e, orb.i, dd
