from multiprocessing import Process, Manager

'''
This case demonstrate that by using Manager().list() to share list of objects between PROCESSES

For the situation I encountered can't be solved by this way cause PickleError raised. the "objects" is not simple one which cPickle doesn't support.

both queue, pipe, manager are using python pickle function to shared objects.

jackw

26/2/2015

'''


class Testonly():
    pass


class ParamHandler():

    def __init__(self):
        self.another_list = []

    def doFirstMP(self):
        self.ID_List = Manager().list()

        process_list = []
        for i in range(5):
            p = Process(target=self.addMP, args=(i,))
            process_list.append(p)

        for p in process_list:
            p.start()

        for p in process_list:
            p.join()



    def addMP(self, kill_id):
        objTest = Testonly()
        self.ID_List.append(objTest)





if __name__ == '__main__':

    paramSet = ParamHandler()
    paramSet.doFirstMP()

    print paramSet.ID_List

