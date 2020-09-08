# Inheritance helps in code reusability and emphasis on DRY principle
# Single Inheritance or Single Level Inheritance
# Apple is base class and MacBook is Derived class
# Attribute search order: Instance Attr -> Class Attr -> Base Class Attributes

class Apple:
    manufacturer = "Apple Inc."
    website = "www.apple.com"

    # @staticmethod
    # def contact():
    #     print("For More info visit: " + Apple.website)

    def contact(self):
        print("For more info visit: " + self.website)
        
        return None


class MacBook(Apple):
    
    def __init__(self):
        self.year_of_manufacture = 2019

    def manufacture_details(self):

        print("This Macbook was Manufactured on {} by {}".format(self.year_of_manufacture,self.manufacturer))

        return None

if __name__ == "__main__":

    macbookair = MacBook()
    print(macbookair.manufacturer)
    print(macbookair.website)
    macbookair.contact()
    
    macbookair.manufacture_details()