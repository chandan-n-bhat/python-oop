# Init and str method
# __init__ is the constructor method
# __str__ is a method that can be used to make a representation for our object

# Need for the constructor method?
class Example:

    def initialiseDetails(self):
        self.name = "My Name"

    def displayDetails(self):
        print(self.name)    # if this method is called before the above method is called it throws an error as the instance attribute is never initialised
    #Thus to avoid such cases, python provides a special method __init__ in which all the attributes are initialised while creating instances.
    # when we create an instance the init method is called by default

class Employee:

    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation
    
    def display_details(self):
        print("Name: " + self.name)
        print("Age:",self.age)
        print("Designation: " + self.designation)

    def __str__(self):
        return str(self.name + ' (' + self.designation +')')


if __name__ == "__main__":

    chandan = Employee("Chandan",21,"SDE-1")
    aarya = Employee("Aarya",18,"Intern")

    print("Employee 1: ",chandan)
    print("Employee 1 Name:",chandan.name)

    print("Employee 2: ",aarya)
    print("Employee 2 designation:",aarya.designation)