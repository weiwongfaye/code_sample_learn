from functools import wraps
def my_decorator(f):
	@wraps(f)
	def warper(*args, **kargs):
		print 'Calling decorated function'
		print 'args are {0}, kargs are {1}'.format(args,kargs)

		return f(*args, **kargs)
	return warper

@my_decorator
def test_no_arg():
	"""test_no_arg"""
	print 'Called test_no_arg function'


@my_decorator
def test_with_arg(*args,**kargs):
	"""test_with_arg"""
	print 'Called test_with_arg function'


test_with_arg(('a','b','c'),a=1,b=2,c=3)
