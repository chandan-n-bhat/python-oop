class Library:
    def __init__(self,name,availableBooks):
        self.name = name
        self.availableBooks = availableBooks
    
    def __str__(self):
        return self.name

    def view_catalogue(self):
        print("\tCatalogue:")
        for i in range(0,len(self.availableBooks)):
            print("\t" + str(i) + " " + self.availableBooks[i])
        print()

        return None

    def request_book(self,book):
        if book not in self.availableBooks:
            print("Sorry! Book currently not available")
        else:
            self.availableBooks.remove(book)
            print("Hope you will like this book!")
        
        return None

    def add_book(self,book):
        if book not in self.availableBooks:
            self.availableBooks.append(book)
        print("Hope you liked the book!")

        return None


class Customer:
    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

    def __str__(self):
        return self.name

    def borrow_book(self):
        self.book = input()
        return self.book
    
    def return_book(self):
        self.book = input()
        return self.book


if __name__ == "__main__":

    print("Welcome To Our Library!")
    print()

    library = Library("Sapna Book House",["Introduction to Python","Let us C","Java Headstart","Algorithms","Datastructures in C++","Cracking the Coding Interview"])

    customer = Customer("Chandan",21,"Software Developer 1")    
    while(True):

        print("Available Operations:")
        print("\t1. View Catalogue")
        print("\t2. Borrow Book")
        print("\t3. Return Book")
        print("\t4. Exit")

        choice = int(input())

        if(choice == 1):
            library.view_catalogue()
            print()

        elif(choice == 2):
            book = customer.borrow_book()
            library.request_book(book)
            print()

        elif(choice == 3):
            book = customer.return_book
        elif(choice == 4):
            print("Thank you for visiting!")
            print()
            break
        else:
            print("Invalid Input")
