class Trace(object):
	def __init__(self):
		self.enabled = True

	def __call__(self,f):
		def wrap(*args, **kargs):
			if self.enabled:
				print "Calling {}".format(f)
			return f(*args, **kargs)
		return wrap

tracer = Trace()
# tracer.enabled = False

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


if __name__ == '__main__':
	l = [1,2,3]
	print rotate_list(l)
	print rotate_list(l)

	print "set tracer.enabeld = false and run again"


