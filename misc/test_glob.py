import glob

print 'Named explicitly:'
for name in glob.glob('/usr/*/*'):
    print '\t', name

print 'Named with wildcard:'
for name in glob.glob('/usr/*'):
    print '\t', name