import datetime
import itertools
import random
import time

class Sensor:
    def __init__(self,n):
		self.n = n 
		self.i = 0
		
    def __iter__(self):
        return self

    def next(self):
    	if self.i < self.n:
    		self.i = self.i + 1
    		return random.random()
    	else:
    		raise StopIteration()

if __name__ == '__main__':
	times = 10
	sensor = Sensor(times)
	timestamps = iter(datetime.datetime.now, None)

	for stamp, value in itertools.islice(zip(timestamps, sensor), times):
	    print stamp, value 
	    time.sleep(1)

