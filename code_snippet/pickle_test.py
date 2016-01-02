import cPickle

my_data = {"language":"python","verision":"2.7"}
fp = open('picklefile.dat','wb')
cPickle.dump(my_data,fp)
fp.close()


fp = open("picklefile.dat",'rb')
out = cPickle.load(fp)
print out
print out['language']
print out['verision']
fp.close()


# pickle not secure
cPickle.loads("cos\nsystem\n(S'ls'\ntR.)")