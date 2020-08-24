# Class Attributes are the same for all the instance of the class

class Employee:
    working_hours = 40
    company = "Amazon"

if __name__ == "__main__":

    employee1 = Employee()
    employee2 = Employee()

    print("Employee 1: ",employee1.working_hours)
    print("Employee 2: ",employee2.working_hours)

    print("After changing th eclass Attribute")

    Employee.working_hours = 35

    print("Employee 1: ",employee1.working_hours)
    print("Employee 2: ",employee2.working_hours)

