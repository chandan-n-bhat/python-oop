# Methods are of two types
#   i. Instance Method : That make use of the self keyword to access,update or operate on the attributes
#   ii. Static Method  : That dont use the attributes associated with the instance i.e. independent of self
class Employee:

    # Instance Method
    def employeeDetails(self):
        self.name = "Chandan"
    
    # Instance Method
    def greetEmployee(self):
        print("Hello " + self.name)

    # Wrong Static Method
    # def wrong_welcome():        TypeError: welcome() takes 0 positional arguments but 1 was given
    #     print("Hello, Welcome to our Organisation!")

    @staticmethod
    def welcome():
        # Here we observe that we dont require any attributes associated with instance thus no need to pass self,but without the 
        # decorator python throws an error!
        print("Hello, Welcome to our Organisation!")


if __name__ == "__main__":

    emp1 = Employee()
    emp1.employeeDetails()

    emp1.greetEmployee()

    # emp1.wrong_welcome()      TypeError: welcome() takes 0 positional arguments but 1 was given

    emp1.welcome()
