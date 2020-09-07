class Employee:
    
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name        


if __name__ == "__main__":

    emp1 = Employee("Chandan")

    print("Object:", emp1)

    print()

    print("Name: " + emp1.get_name())

    emp1.set_name("Chandan N Bhat")

    print("Name: " + emp1.get_name())
