def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # for uncahngeable vars here, python will think it is a local vars
        # therefore you will get unboundlocalerror. for list, dict, it is fine to use
        # but for unmutable types, you must declare nonlocal as below for using the closure
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

if __name__ == "__main__":
   avg = make_averager()
   print(avg(10))
