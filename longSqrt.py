#author 	: https://github.com/Brouss3
#date start	: 2018/01/30
#date end	: 2018/02/03
#version	: 0.0
#licence    : GPL
from math import sqrt as msqrt,log as mlog


#original seed square root function
def sqNear0(lf):
    assert(lf>=0)
    d=int(mlog(lf,10))
    r0=10**((d)//2)
    if(r0**2>lf ):
        assert(False)
    fl=lf*10**(2*10)//r0**2
    fl=msqrt(fl)
    r1=r0*int(fl*10**10)//10**20
    return(r1)

#after a while I thought I made the seed overcomplicated
def sqNear1(lf):
    le=int(mlog(lf,10)//2)*2
    if le <100:
        return(int(msqrt(lf)))
    a=lf//10**(le-100)
    return(int(msqrt(a))*10**((le-100)//2))
    
#looping function
def lsqrt(v,seed=sqNear0):               
    assert(v>=0)
    if v<1:
        return(0L)
    r=seed(v)    
    r=min(r,v//r)
    while (r+1)**2<v:
        r+=int((v//r+1-r)/2)
        r=min(r,v//r)
    return(r)

