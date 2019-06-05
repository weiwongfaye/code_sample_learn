from random import randint
# def d6():
#     return randint(1, 6)

# d6_iter = iter(d6, 1)
# for roll in d6_iter:
#     print(roll)


max_try = 10
while max_try > 0:
    try:
        a = randint(1,6)
        print(a)
        assert a > 9
        break
    except Exception as e:
        e = e
        max_try = max_try - 1
    
if max_try == 0: 
    raise Exception("connection issue")
print("pass")