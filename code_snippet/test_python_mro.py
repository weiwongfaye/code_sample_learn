class A(object):
	def show(self):
		print "A.show()"
	def get_final_show(self):
		self.show()
class B(A): pass
class C(A):
	def show(self):
		print "C.show()"
		self.show()
class D(B, C): pass
print D.__mro__
d = D()
d.get_final_show()