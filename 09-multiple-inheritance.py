# The derived class can inherit from multiple base classes.
# For example a child can inherit Business skills from his Father and similarly Cooking skills from his mother.
# class Child(Father,Mother):

class OperatingSystem():
    multitasking = True
    gui = True

    def shutdown(self):
        print("Shutting Down...")
        return None

    def restart(self):
        print("Restarting...")
        return None


class Apple():
    
    def __init__(self):
        self.manufacturer = "Apple Inc."
        self.website = "www.apple.com"

    def contact(self):
        print("For more info visit " + self.website)
        return None

class Macbook(OperatingSystem,Apple):

    def __init__(self):
        self.year_of_manufacture = 2019
        Apple.__init__(self)    # To invoke the __init__ of Apple, Operating system doesnt have a __init__

    def display_specs(self):
        print("This Macbook was manufactured on {} by {}".format(self.manufacturer,self.year_of_manufacture))
        print("Operating System: \nMultitasking:{} \nGUI:{}".format(self.multitasking,self.gui) )
        return None

if __name__ == "__main__":

    macbook_air = Macbook()
    macbook_air.display_specs()