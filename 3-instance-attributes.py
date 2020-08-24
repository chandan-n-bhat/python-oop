# Instance attributes are those which are specific to an instance of the class

class Employee:

    # class attribute
    working_hours = 40
    company_name = "Amazon"

if __name__ == "__main__":

    emp1 = Employee();

    emp1.name = "Chandan"

    print("Emp1 Name: ",emp1.name)

    emp2 = Employee()
    # print("Emp2 Name: ",emp2.name)    # throws an attribute error (AttributeError: 'Employee' object has no attribute 'name')

    # creating instance variable for emp2
    emp2.name = "Aarya"
    print("Emp2 Name: ",emp2.name)

    # WHat happens in the below case
    print("Emp1 working hours: ",emp1.working_hours)
    print("Emp2 working hours: ",emp2.working_hours)

    print("After changing")

    emp1.working_hours = 35     # This creates a new instance variable for emp1 object thus not affecting any class variables of other objects

    # Python first checks for instance attributes and the for class attributes and then throws an error if not found
    # Thus if both instance and class attributes have the same name then instance attribute wins over the class attribute
    print("Emp1 working hours: ",emp1.working_hours)
    print("Emp2 working hours: ",emp2.working_hours)

