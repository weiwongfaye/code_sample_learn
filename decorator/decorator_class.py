class CallCount(object):
	def __init__(self, f):
		self.f = f
		self.count = 0

	def __call__(self,*args, **kargs):
		self.count += 1
		return self.f(*args, **kargs)

@CallCount
def hello(name):
	print 'hello, {name}'.format(name=name)



if __name__ == '__main__':
			hello('test1')	
			hello('test2')
			hello('test3')
			print hello.count

