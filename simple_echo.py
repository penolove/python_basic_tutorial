import sys

argv=sys.argv
if len(argv)==2:
	x=argv[1]
	for i in range(5):
		print x
elif(len(argv)>2): 
	print "don't give me too much variables"
else:
	print "one variable thx."
