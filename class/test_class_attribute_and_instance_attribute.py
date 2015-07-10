class A (object):
	"""
	this is doc string test
	"""
	# inmutable value
	data = "abc"
	# mutable value
	objectlist = []

	def __init__(self):
	    self.objectlist.append(self)
	pass

myobj1 = A()
myobj2 = A()
print myobj1.objectlist
print myobj2.objectlist
print A.objectlist

print myobj1.data
print myobj2.data
print A.data
print myobj1.__dict__
myobj1.data = "myobj1"
myobj2.data = "myobj2"

print myobj1.data
print myobj2.data
print A.data

print myobj1.__dict__
print myobj2.__dict__
print A.__dict__

print myobj1.__dict__
myobj1.testnewvalue = "testnewvalue"
myobj1.__setattr__("testnewvaluefromsetattr","testnewvaluefromsetattr")
print myobj1.__getattribute__("testnewvalue")
print myobj1.__getattribute__("testnewvaluefromsetattr")
print myobj1.__dict__ 


