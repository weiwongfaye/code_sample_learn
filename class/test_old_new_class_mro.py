# old style class mro

class Aold:
	def __init__(self):
		print "A default constructor"
class Bold(Aold): 
	pass
class Cold(Aold):
	def __init__(self):
	    print "C default constructor"

class Dold(Bold, Cold):
        pass

dold = Dold()
# Dold.__mro__

# new class style mro example
class A(object):
	def __init__(self):
		print "A default constructor"
class B(A): 
	pass
class C(A):
	def __init__(self):
	    print "C default constructor"

class D(B, C):
        pass

d = D()

print D.__mro__
