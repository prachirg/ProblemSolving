'''Write an object oriented program that performs the following tasks:
1. Create a class called Chair from the base class Furniture
2. Teakwood should be the type of furniture that is used by all furnitures by
default
3. The user can be given an option to change the type of wood used for chair if
he wishes to
4. The number of legs of a chair should be a property that should not be altered
outside the class'''

class Furniture:
    typeOfFurniture = "Teakwood"

class Chair(Furniture):
    __numberOfLegs = 4
    def __init__(self):
        print("Change type of wood to another from {}?".format(self.typeOfFurniture))
        response = input()
        if response=='Y' or response=='Yes':
            self.typeOfFurniture = 'Oak'
        print("Chair private: number of legs:",self.__numberOfLegs)

furniture = Furniture()
print("Furniture wood type:",furniture.typeOfFurniture)
chair = Chair()
print("Chair wood type",chair.typeOfFurniture)
#print(chair._Chair__numberOfLegs)




