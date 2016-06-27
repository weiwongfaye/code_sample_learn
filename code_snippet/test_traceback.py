import traceback
mylist = ['a','b']
try:
	del mylist[2]
except IndexError as ex:
	print "exception happen, index out of range"
	print ex
	traceback.print_exc()
	print traceback.format_exc()
	