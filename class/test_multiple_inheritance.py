class A(object):
	"""docstring for A"""
	def __init__(self, arg):
		self.arg = arg
	def __str__(self):
		return "this is A"

	def test():
		print "this is A test"


class B(object):
	"""docstring for B"""
	def __init__(self, arg):
		self.arg = arg
				
	def __str__(sef):
		return "this is B"

	def test(self):
		print "this is B test"


class C(A,B):
	"""docstring for C"""
	def __init__(self, arg):
		super(C, self).__init__(arg)
		self.arg = arg
	def __str__(self):
		return "this is C"

	def test(self):
		print "this is C test"



c = C('testC')
print help(c)
C.__bases__[1].test(B("testb"))
c.__class__.__bases__[1].test(B("testb"))