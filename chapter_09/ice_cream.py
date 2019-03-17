class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Name: ",self.restaurant_name)
        print("Type: ",self.cuisine_type)

class Ice_Cream(Restaurant):

    def __init__(self,name,cuisine_type,flavours):
        super().__init__(name,cuisine_type)
        self.flavours = flavours
    
    def availabe_flavours(self):
        for flavour in self.flavours:
            print(flavour.title())

flavours = ['chocolate','vanilla']
ice = Ice_Cream('Ice Cream Corner', 'Ice cream', flavours)
ice.availabe_flavours()


