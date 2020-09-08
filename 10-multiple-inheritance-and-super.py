class Father:
    def __init__(self):
        print("Start: Father __init__")
        self.fatherAttribute = "Attr1"
        print("End: Father __init__")
        
    def work(self):
        print("Working...")

        
class Mother:
    def __init__(self):
        print("Start: Mother __init__")
        self.motherAttribute = "Attr2"
        print("End: Mother __init__")

    def cook(self):
        print("Cooking...")


class Child(Mother,Father):
    def __init__(self):
        print("Start: Child __init__")
        # super().__init__()    #This may not work
        Mother.__init__(self)
        Father.__init__(self)
        self.childAttribute = "Attr3"
        print("End: Child __init__")
    
    def play(self):
        print("Playing...")
        
boy = Child()
# print(x.graduationyear)

boy.cook()
boy.work()
boy.play()

print("Attribute Inherited from Father:",boy.fatherAttribute)
print("Attribute Inherited from Mother:",boy.motherAttribute)
print("Attribute of Child:",boy.childAttribute)

