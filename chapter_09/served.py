class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = False
        self.number_served = 0

    def describe_restaurant(self):
        print("Name: ",self.restaurant_name)
        print("Type: ",self.cuisine_type)

    def is_open(self):
        return self.open

    def open_restaurant(self):
        self.open = True
        print("Restaurant is now open!")

    def set_number_served(self,number):
        if self.is_open() and number > 0:
            self.number_served = number
        else:
            print("Closed restaurant can't take customers")

    def increment_number_served(self,number):
        if number < 0:
            print("Incompatible Value")
            return
        else:
            self.set_number_served(number)
        
restaurant = Restaurant("Happy Lotus","Chinese")
print(restaurant.number_served)
restaurant.number_served = 50
print(restaurant.number_served)

restaurant.number_served = 0
restaurant.set_number_served(50)
restaurant.open_restaurant()
restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.number_served = 0
restaurant.increment_number_served(50)
print(restaurant.number_served)
