class master(object):
    """
    this is doc string test
    """

    def __init__(self):
        self._master_url = None
        self._management_port = None


    def add_peer(self, peer):
        pass

    def remove_peer(self,peer):
        pass

    def notice_peer(self,peer):
        pass

    def __repr__(self):
        return "repr string for obj"

    def __str__(self):
        return "str string for obj"


    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value

    @property
    def master_url(self):
        return self._master_url

    @master_url.setter
    def master_url(self,value):
        self._master_url = value

    @property
    def management_port(self):
        return self._management_port

    @management_port.setter
    def management_port(self,value):
        self._management_port = value


class peer(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    master = master()
    print master.master_url
    master.master_url = "test"
    print master.master_url

    print master.management_port
    master.management_port = '8091'
    print master.management_port

    print master.__dict__

    # add new attribute
    master.test_port = "8100"
    print master.__dict__

    # master._master_url = 'master_url_string'
    # print master.__dict__
    # # print master.__class__
    # # print master.__doc__
    # # # print master.__repr__()
    # # print repr(master)
    # # print str(master)
    # print master.__getattribute__('_master_url')
    #
    # master.__setattr__('master_url','test')
    # print master.__dict__
    # print master.__getattribute__('master_url')

