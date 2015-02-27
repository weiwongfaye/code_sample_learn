"""
python dispatcher example
27/2/2015 

"""

class Dispatcher:

    def do_get(self): 
        print "do_get"

    def do_put(self, item):
        print "do_put %s" % item


    def error(self):
        print "error"

    def dispatch(self, command):
        mname = 'do_' + command
        if hasattr(self, mname):
            method = getattr(self, mname)
            return method
        else:
            self.error()

if __name__ == '__main__':
    
    ds = Dispatcher()
    get_function = ds.dispatch("get")
    get_function()

    put_function = ds.dispatch("put")
    put_function("aaa")
