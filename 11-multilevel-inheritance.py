class MusicalInstrument:
    no_of_major_keys = 12

class StringInstrument(MusicalInstrument):
    type_of_wood = "Tone Wood"

class Guitar(StringInstrument):
    def __init__(self,strings):
        self.no_of_strings = strings
        print("This Guitar consists of {} Major Keys".format(self.no_of_major_keys))
        print("This Guitar consists of {} strings".format(self.no_of_strings))
        print("This Guitar is made of {}".format(self.type_of_wood))

if __name__ == "__main__":

    g1 = Guitar(6)

    # print(g1.no_of_major_keys)
    # print(g1.type_of_wood)
    # print(g1.no_of_strings)
