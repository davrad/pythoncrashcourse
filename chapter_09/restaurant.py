class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = False

    def describe_restaurant(self):
        print("Name: ",self.restaurant_name)
        print("Type: ",self.cuisine_type)

    def open_restaurant(self):
        self.open = True
        print("Restaurant is now open!")

res1 = Restaurant("Happy Lotus","Chinese")
res2 = Restaurant("Dancing Sombrero","Mexican")
res3 = Restaurant("Feisty Pretzel","German")

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()
