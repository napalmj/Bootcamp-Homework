

class Car:
    manufacturer = 'Skomda'
    doorList = [2, 4, 5]
    def __init__(self, doorCount: int, driveType: int, color: str, cylinderCount: int):
        self.doorCount = doorCount
        self.driveType = driveType
        self.color = color
        self.cylinderCount = cylinderCount

    def printCarStats(self):
        print('Doors', self.doorCount)
        print('Drive Type', self.driveType)
        print('Color', self.color)
        print('Cylinders', self.cylinderCount)
        print('')

carModel1 = Car(2, 2, 'blue', 4)
carModel2 = Car(2, 2, 'green', 6)
carModel3 = Car(5, 4, 'blue', 6)

carModel1.printCarStats()
carModel2.printCarStats()
carModel3.printCarStats()

print(type(carModel1))