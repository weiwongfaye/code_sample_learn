def reverse_list(l):
	while len(l) > 0:
		yield l.pop()


mylist = ['a','b','c','d']


for item in reverse_list(mylist):
	print item


rList = reverse_list(mylist)
print help(rList)
