# Put in const.py...:
class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass
    		
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const(%s)"%name
        if not name.isupper():
        	raise self.ConstCaseError, "Const name %s is not all uppercase".format(name)
        self.__dict__[name]=value

import sys
# ref = sys.modules[__name__]
# print sys.modules[__name__]
sys.modules[__name__]=_const()


# ****************************************
# DEFINE CONSTANT IN THIS FILE (const.py)
# ****************************************

import const
# and bind an attribute ONCE:
const.MAGIC = 23
const.MY_CONSTANT_TEST = 33


# ****************************************
# On Client, use the const as below

# # that's all -- now any client-code can
# import const
# # and bind an attribute ONCE:
# const.TEST = 33
# # but NOT re-bind it:
# # const.magic = 88      # raises const.ConstError
# # you may also want to add the obvious __delattr__
# const.MAGIC = 33

# ****************************************





