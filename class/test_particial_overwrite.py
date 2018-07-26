from abc import ABCMeta, abstractmethod

class TestClass(object):
	"""docstring for TestClass"""

	__metaclass__ = ABCMeta
	def __init__(self):
		super(TestClass, self).__init__()
		
	def mytestFunction(self):
		print "A"
		pass


class SubTestClassA(TestClass):
	pass


class SubTestClassB(TestClass):
	"""docstring for SubTestClassB"""
	def __init__(self):
		super(SubTestClassB, self).__init__()

	def mytestFunction(self):
		super(SubTestClassB, self).mytestFunction()
		print "B"

# can't instance 
myobj = TestClass()
# can't instance
myobj = SubTestClassA()
# okay
myobj = SubTestClassB()
myobj.mytestFunction()