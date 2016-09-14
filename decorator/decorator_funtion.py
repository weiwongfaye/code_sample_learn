import functools

def mystrip(f):
	@functools.wraps(f)
	def wrap(*args, **kargs):
		return f(*args, **kargs).strip()
	return wrap


def test1(par1):
	return par1

@mystrip
def test2(par1):
	'test2 doc string'
	return par1


if __name__ == '__main__':
	print test1(' ha haf ')
	print test2(' ha haf ')


	# functools test2
	print test2.__name__
	print test2.__doc__