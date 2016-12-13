class Bike(object):
    def __init__(self, price,speed,miles=0):
        print ('New Bike')
        self.price = price
        self.speed = speed
        self.miles = miles
    def displayInfo(self):
        print ('Price: {} Max Speed: {} Miles: {}'.format(self.price,self.speed,self.miles))
        return self
    def ride(self):
        self.miles += 10
        print ('Riding {}'.format(self.miles))
        return self
    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print ('Reversing {}'.format(self.miles))
        return self

bike1 = Bike(100,25)
bike1.ride().ride().ride().reverse().displayInfo()
