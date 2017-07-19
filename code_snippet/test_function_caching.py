import functools
def memoize(func):
    """
    Cache the results of the function so it doesn't need to be called
    again, if the same arguments are provided a second time.
    """
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        # This line is for demonstration only.
        # Remove it before using it for real.
        print 'Calling %s()' % func.__name__
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def multiply(x,y):
    print "in multiply"
    return x*y

if __name__ == "__main__":
    multiply(2,3)
    multiply(3,4)
    multiply(2,3)
