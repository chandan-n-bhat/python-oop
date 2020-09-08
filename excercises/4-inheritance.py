class Furniture:
    def __init__(self):
        self.type_of_wood = "Teakwood"

class Chair(Furniture):
    
    def __init__(self):
        super().__init__()
        self.__no_of_legs = 4

    def set_wood_type(self,wood_type):
        self.type_of_wood = wood_type
        return None
    
    def get_wood_type(self):
        return self.type_of_wood

    def display_specs(self):
        print("This chair is made of {} wood type and has {} legs".format(self.type_of_wood,self.__no_of_legs))
        return None

if __name__ == "__main__":

    chair = Chair()
    print("Default Wood Type:",chair.get_wood_type())

    choice = input("Would you like to Customise the wood of your chair(Y/N):")

    if choice in ['y','Y']:

        #Change wood type to Saghvani
        wood_type_input = input("Enter the type of wood: ")
        chair.set_wood_type(wood_type_input)
        print("Wood Type after customization:",chair.get_wood_type())


    # print("No of Legs:",chair.__no_of_legs)     #Attribute error
    # print("No of Legs:",chair._Chair__no_of_legs)     #Works but not adviced
    chair.display_specs()