def mystrip(f):
	def wrap(*args, **kargs):
		return f(*args, **kargs).strip()
	return wrap


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


@tracer
@mystrip
def test1(par1):
	return par1


if __name__ == '__main__':
	print test1(' xfee ds ')