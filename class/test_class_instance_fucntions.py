class A(object):
	pass

class B(A):
	def __init__(self):
		super(B,self).__init__()
		self.foo = 100

	def __str__(self):
		return "this is B __str__"

	def __repr__(self):
		return "this is B __repr__"

	pass


if __name__ == '__main__':
	
	# check if B is subclass of A
	print issubclass(B,A)

	# check if a is instance of A
	a = A()
	b = B()

	print isinstance(a,A)
	print isinstance(b,B)
	print isinstance(a,B)

	# hasattr(), getattr(),setattr(), delattr()

	if hasattr(b,"foo"):
		print getattr(b,"foo")
		print "changing foo attribute value.."
		setattr(b,"foo",200)
		print getattr(b,"foo")
		print "deleting foo attribute.."
		delattr(b,"foo")
		print getattr(b,"foo","Not found!")
		# add new attribute
		setattr(b,"bar","300")
		print getattr(b,"bar")

	else:
		print "no attribute: foo"


	# vars() and __dict__, vars equal __dict__
	print vars(b)
	print b.__dict__
	# while no parameter given, it equal locals
	print vars()
	print locals()



	# str() and repr()
	print str(b)
	print b
	print repr(b)
	print str(a)

		