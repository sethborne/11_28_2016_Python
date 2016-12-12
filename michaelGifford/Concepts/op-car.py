class Car(object):
    def __init__(self, price,speed,fuel,mileage):
        print ('New Car')
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print ('Price: {}'.format(self.price))
        print ('Speed: {}'.format(self.speed))
        print ('Fuel: {}'.format(self.fuel))
        print ('Mileage: {}'.format(self.mileage))
        print ('Tax: {}'.format(self.tax))


car1 = Car(8000,100,'Full',100345)
car1.display_all()

car1 = Car(35000,120,'Full',1356)
car1.display_all()

car1 = Car(10000,105,'Full',54861)
car1.display_all()

car1 = Car(5500,110,'Full',98214)
car1.display_all()

car1 = Car(9999,100,'Full',43102)
car1.display_all()

car1 = Car(999,80,'Full',19990)
car1.display_all()
