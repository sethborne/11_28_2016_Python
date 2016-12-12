class Bike(object):
    def __init__(self, price,speed,miles=0):
        print ('New Bike')
        self.price = price
        self.speed = speed
        self.miles = miles
    def displayInfo(self):
        print ('Price: {} Max Speed: {} Miles: {}'.format(self.price,self.speed,self.miles))
    def ride(self):
        self.miles += 10
        print ('Riding {}'.format(self.miles))
    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print ('Reversing {}'.format(self.miles))

bike1 = Bike(100,25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
