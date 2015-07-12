class RoundFloat(float):
	# the __new__ method should always be class method
     def __new__(cls, val):
		return super(RoundFloat, cls).__new__(cls, round(val, 2))	


if __name__ == '__main__':
	print RoundFloat(1.46238)
	print RoundFloat(0)
	print RoundFloat(1.2593)

	print RoundFloat.__mro__