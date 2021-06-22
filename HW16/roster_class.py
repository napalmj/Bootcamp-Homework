import random as rd


class RosterClass:

    firstNamesList = [
        'Alfred',
        'Marty',
        'Emmett',
        'Jon',
        'Luke'
        ]
    lastNamesList = [
        'Hanson',
        'McFly',
        'Brown',
        'Snow',
        'Skywalker'
        ]
    breedList = [
        'McLaren',
        'Ferrari',
        'Lamborghini',
        'Porsche',
        'Mercedes-Benz',
        'Maserati'
        ]
    colorList = [
        'Coquelicot',
        'Vermilion',
        'Glaucous',
        'Celadon',
        'Amaranth',
        'Skobeloff'
        ]
    medicalConditionList = [
        'Pica',
        'Morgellons Disease',
        'Heartworm',
        'Leptospirosis',
        'Rabies'
        ]

    def __init__(
        self,
        firstName='',
        lastName='',
        weight='',
        breed='',
        age='',
        color='',
            medicalCondition=''):
        self.firstName = firstName or rd.choice(self.firstNamesList)
        self.lastName = lastName or rd.choice(self.lastNamesList)
        self.weight = weight or rd.randint(1, 100)
        self.breed = breed or rd.choice(self.breedList)
        self.age = age or rd.randint(1, 20)
        self.color = color or rd.choice(self.colorList)
        self.medicalCondition = medicalCondition or rd.choice(
            self.medicalConditionList
            )

    def printMedicalChart(self):
        print('(First Name):', self.firstName)
        print('(Last Name):', self.lastName)
        print('(Weight):', str(self.weight) + 'lbs')
        print('(Breed):', self.breed)
        print('(Age):', self.age)
        print('(Color):', self.color)
        print('(Medical Condition):', self.medicalCondition)

    def changeName(self, firstValue, secondValue):
        self.firstName = firstValue
        self.lastName = secondValue


def generateClassInstance(
    objectInstance: type,
    sizeOfInstancesGenerated: int,
        values=[]):
    generationList = []
    for i in range(sizeOfInstancesGenerated):
        generationList.append(objectInstance(*values))
    return generationList


def printNames(rosterList: list):
    for n in range(len(rosterList)):
        print(f'{n+1}:', rosterList[n].firstName, rosterList[n].lastName)
