
Goals: 
======

* Calculate square roots of large integer numbers in acceptable time.
(Been told I was O(log(n)²) based on chronoed operations)

* Create my first github repo

Usage:
======
    
from longSqrt import lsqrt,sqNear1
# (sqNear1 optional, for alternate seed sqrt func)
x=119**300+11**9999+7**53   #or any long int
print(lsqrt(x))                  #voila
y=lsqrt(x,sqNear1)
print(y)


Last word:
==========

Yes, that's short. But it's for a 20 line prog...
