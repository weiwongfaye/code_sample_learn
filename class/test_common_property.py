class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


myobj = C()
myobj.x = "tes1t"
print myobj.x 
print myobj._x
print myobj.__dict__
del myobj.x
print myobj.__dict__
