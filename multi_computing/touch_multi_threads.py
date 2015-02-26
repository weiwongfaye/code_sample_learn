from threading import Thread, Lock

'''
This case demonstrate that by using thread instead of process, value is shared automatically.
jackw
@ 25/2/2015
'''


class Testonly():
    pass


class ParamHandler():

    def __init__(self):
        self.ID_List = []
        self.lock = Lock()

    def doFirstMP(self):

        thread_list = []
        for i in range(5):
            p = Thread(target=self.addMP, args=(i,))
            thread_list.append(p)

        for p in thread_list:
            p.start()

        for p in thread_list:
            p.join()



    def addMP(self, kill_id):
        objTest = Testonly()
        self.lock.acquire()
        self.ID_List.append(objTest)
        self.lock.release()




if __name__ == '__main__':

    paramSet = ParamHandler()
    paramSet.doFirstMP()

    print paramSet.ID_List

