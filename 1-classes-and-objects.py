# CHeck if the employee has achieved his weekly target or not

class Employee:

    name = "Chandan"
    age = 21
    designation = "Software Developer I"
    appsMadeThisMonth = 3

    def achievedTarget(self):
        
        if(self.appsMadeThisMonth > 2):
            return "Target Achieved!!"
        else:
            return "Target Failed!!"

if __name__ == "__main__":

    employee1 = Employee()
    print("Name: ",employee1.name)
    print("Age: ",employee1.age)
    print("Designation: ",employee1.designation)
    print("Status: ",employee1.achievedTarget())