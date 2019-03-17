class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self):
        self.size = 70
    def upgrade(self,new):
        self.size = new
    def get_size(self):
        print(self.size)

class Electric_Car(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    
    def upgrade_battery(self,size):
        self.battery.upgrade(size)

    def get_size(self):
        self.battery.get_size()

electric = Electric_Car('foo','bar',2019)

electric.get_size()
electric.upgrade_battery(100)
electric.get_size()