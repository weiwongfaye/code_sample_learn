from collections import Counter

c = Counter("this is test string")

# list of first 2 common charactors
print c.most_common(2)

# get key
print c.keys()

# get key's value
print c.get('t')

# iter
for k in c.keys():
	print "key {key} appear {times}".format(key = k,times = c.get(k))

# most common
print c.most_common(1)