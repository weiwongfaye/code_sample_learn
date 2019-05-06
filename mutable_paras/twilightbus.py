class TwilightBus(object):
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            #dangeours: use mutable object as parameters 
            #self.passengers = passengers
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    basketball_team = ['sue', 'tina', 'maya', 'diana', 'pat']
    print('before:{}'.format(basketball_team))
    bus = TwilightBus(basketball_team)
    bus.drop('tina')
    bus.drop('maya')
    print('after:{}'.format(basketball_team))
