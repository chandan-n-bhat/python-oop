class Car_Rental:
    
    def __init__(self):
        # Why car_type is instance attribute? Cause rent may vary for different Car Rental company. Here Hardcoded for simplicity
        self.car_type = {"Hatchback":30,"Sedan":50,"SUV":100}
    

    def calculate_fare(self,car,days):
        
        if car not in self.car_type:
            print("Invalid Car type!")
        else:
            print("Fare:",self.car_type[car]*days)

        return None
    

    def display_fare(self):
        print()
        print("Fare per day:")
        for i in self.car_type.keys():
            print(i,":",self.car_type[i],"Rs")
        print()

        return None

if __name__ == "__main__":

    car_rent1 = Car_Rental()
    print()
    print("Welcome to Car Rental Service")
    while(True):

        print("1. Display Car Fare")
        print("2. Calculate Fare")
        print("3. Exit")

        choice = int(input())

        if(choice == 1):
            car_rent1.display_fare()
        
        elif(choice == 2):
            car = input("Enter the car type:")
            days = int(input("Enter the number of days:"))
            car_rent1.calculate_fare(car,days)
            print()
        
        elif(choice == 3):
            print("Thank you for visiting")
            break
        
        else:
            print("Invalid Choice!")
            print()