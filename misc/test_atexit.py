import atexit

def all_done():
	print "all done ()"

def clean_up(name):
	print "my clean up %s" % name
 
print "registering all_done"
atexit.register(all_done)
print "registered all_done"

atexit.register(clean_up, 'first')
atexit.register(clean_up,'second')
atexit.register(clean_up,'third')
