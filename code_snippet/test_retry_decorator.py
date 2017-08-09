from functools import wraps
import time
tries_least = 1

def retry_request(tries=5, delay=3, backoff=2):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            _tries, _delay = tries, delay

            global tries_least
            if _tries < tries_least: _tries=tries_least
            print _tries
            while _tries >= 1:
                try:
                    return f(*args, **kwargs)
                except TestFailure, e:
                    msg = "{}, Retrying in '{}' seconds...".format(
                            str(e), _delay)
                    print msg
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            return f(*args, **kwargs)
        return f_retry  
    return deco_retry

@retry_request(tries=tries_least)
def test_f():
    raise TestFailure("Exception happen")


class TestFailure(Exception):
    pass    


def change_tries(tries):
    global tries_least
    tries_least=tries




if __name__ == '__main__':
    change_tries(3)
    test_f()
