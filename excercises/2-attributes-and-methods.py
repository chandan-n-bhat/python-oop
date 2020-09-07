class Precious_Stone:

    count = 0
    stones = list()

    def __init__(self,name):
        self.name = name
        Precious_Stone.count += 1
        Precious_Stone.stones.append(self.name)
        if len(Precious_Stone.stones) > 5:
            Precious_Stone.stones.pop(0)
            Precious_Stone.count -= 1


    def __str__(self):
        return self.name

    @staticmethod
    def check_stones():
        print("Count: " + str(Precious_Stone.count) + "(" + str(len(Precious_Stone.stones)) + ")")

    @staticmethod
    def print_stones():
        print("Stones:",end="")
        for i in Precious_Stone.stones:
            print(i,end=" ")
        print()

if __name__ == "__main__":

    s1 = Precious_Stone("Diamond")
    s2 = Precious_Stone("Ruby")
    s3 = Precious_Stone("Emarald")
    s4 = Precious_Stone("Gem Stone")
    
    s4.check_stones()
    s4.print_stones()

    s5 = Precious_Stone("Pearl")
    s4.print_stones()
    s4.check_stones()

    s6 = Precious_Stone("White Stone")
    s4.print_stones()
    s4.check_stones()