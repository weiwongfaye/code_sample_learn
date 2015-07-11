from abc import ABCMeta, abstractmethod

class TestClass(object):
	"""docstring for TestClass"""

	__metaclass__ = ABCMeta
	def __init__(self):
		super(TestClass, self).__init__()
		
	# define pure vitural method
	@abstractmethod
	def myVirturalMethod(self):
		pass


class SubTestClassA(TestClass):
	pass


class SubTestClassB(TestClass):
	"""docstring for SubTestClassB"""
	def __init__(self):
		super(SubTestClassB, self).__init__()

	def myVirturalMethod(self):
		print "method in SubTestClassB"

# can't instance 
myobj = TestClass()
# can't instance
myobj = SubTestClassA()
# okay
myobj = SubTestClassB()
myobj.myVirturalMethod()