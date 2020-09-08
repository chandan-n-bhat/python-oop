# Access Specifiers: Public, Private and Protected
# Public : Accessible inside the class, Derived class and anywhere outside the derived class => name
# Protected : Accessible inside the class and Derived class only => _name
# Private : Only by the class and not the derived class also => __name

# Note : Python doesnot impose syntactical rules to access specifiers and is just a naming convention followed. A private attribute in the class
#        can be used anywhere and is not restricted by python syntax. But it isnt a good practice to do so 
class Car:
    no_of_wheels = 4
    _color = "Black"
    __year_of_manufacture = 2019

    def get_year(self):
        print("Year:",self,__year_of_manufacture)

class BMW(Car):

    def getColor(self):
        print("Color of the car:",self._color)

if __name__ == "__main__":


    car1 = Car()
    print("Public:",car1.no_of_wheels)

    # print("Protected:",car1._color)   # This works but is not a good practice

    bmw1 = BMW()
    bmw1.getColor()

    # print("Private Attribute: ",car1.__year_of_manufacture)   #AttributeError: 'Car' object has no attribute '__year_of_manufacture'
    # Python prepends _Car in this case to the private attribute. Thus this error can be overcome but it is not a good practice to do so.
    # This is called Name Mangling of private variables _ClassName__privateattribute
    print("Overcomming Private Attribute:",car1._Car__year_of_manufacture)  # Higly not recommended


