#!~/anaconda2/bin/python
import sys


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


argv=sys.argv
if len(argv)==3:
	result=gcd(int(argv[1]),int(argv[2]))
	print "gcd is :" +str(result)
elif(len(argv)>3): 
	print "don't give me too much variables"
else:
	print "one variable thx."

