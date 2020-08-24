# The Self keyword

class Employee:

    # Method without self, throws error
    # def employeeDetails():
    #     pass

    def foobar(self):
        self.name = "Chandan"
        self.age = 21

        print("Name :",self.name)
        print("Age :", self.age)
        
    def attributeWithoutSelf(self):

        self.attr1 = "Attr1"
        attr2 = "Attr2"

        print("Attribute 1:",self.attr1)
        print("Attribute 2:",attr2)

class Student:

    def student_details(self):
        self.name = "Student1"
        self.age = 18
        marks = 94      # This attribute is equivalent to a variable whose scope is limited within this method!
    
    def display_details(self):
        print("Displaying "+ str(self) + " Details")
        print("Name :",self.name)
        print("Age :",self.age)
        # print("Marks :",marks)

if __name__ == "__main__":

    emp1 = Employee()
    #emp1.employeeDetails()  #TypeError: employeeDetails() takes 0 positional arguments but 1 was given

    #the above call to the method is equivalent to Employee.employeeDetails(emp1) i.e. Class.method(object-instance)
    # Thus by defaul a parameter(the instance itself) is passed

    emp1.foobar()

    emp1.attributeWithoutSelf()

    # We observer that even though we initialise an attribute without the self keywork we dont get any error.
    # But when we create an instance attribute we expect it to be present in the entire lifecycle of the instance object
    # In the above case the attribute attr2 is just like a regular variable whose scope is limited to the method attributeWithoutSelf()

    # Another example for lifecycle of an attribute initialise without self keyword
    student1 = Student()

    student1.student_details()
    student1.display_details()  # NameError: name 'marks' is not defined, as its scope is limited to student_details() method and not the entire instace lifecycle

    # An object instance lifecycle is from it being initialised to it being deleted or the program being terminated