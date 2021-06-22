import roster_class

dogRoster = roster_class

listOfDogRosters = dogRoster.generateClassInstance(dogRoster.RosterClass, 5)

while 1:
    rosterLength = len(listOfDogRosters)
    dogRoster.printNames(listOfDogRosters)
    dogRosterSelection = input(
        '(1): Add dog to roster: \n(2): Select a dog to view:\n'
        )
    print('')

    if int(dogRosterSelection) == 1:
        firstName = input('First Name: ')
        lastName = input('Last Name: ')
        weight = input('Weight: ')
        breed = input('Breed: ')
        age = input('Age: ')
        color = input('Color: ')
        medicalCondition = input('Medical Condition: ')

        listOfDogRosters.append(
            dogRoster.RosterClass(
                firstName,
                lastName,
                weight,
                breed,
                age,
                color,
                medicalCondition
                )
            )
        print('')

        listOfDogRosters[5].printMedicalChart()
    elif int(dogRosterSelection) == 2:
        dogRoster.printNames(listOfDogRosters)
        print('')
        rosterViewSelection = input(
            f'Select 1 - {rosterLength} to view roster: '
            )

        listOfDogRosters[int(rosterViewSelection) - 1].printMedicalChart()

    print('')
    escapeScript = input(
        'Enter ''Q'' to Escape:\nEnter A Character to Continue: '
        )
    if escapeScript == 'Q':
        print('Thank you for using Medical Roster for Dogs!')
        quit()
