def showMenu():
    print('\nContact list:')
    print('1. Add new contact')
    print('2. Delete contact ')
    print('3. Search contact')
    print('4. Show contact list ')
    print('5. Exit')
    print('')

def Main():
    contactList = {}

    while True:
        showMenu()
        optionChoosen = input('Please choose an option ')
        print('')

        if optionChoosen == '1':
            addNewContact(contactList)
        elif optionChoosen == '2':
            removeContact(contactList)
        elif optionChoosen == '3':
            searchContact(contactList)
        elif optionChoosen == '4':
            showContactList(contactList)
        elif optionChoosen == '5':
            print('Exiting... Bye bye!')
            break
        else:
            print('Type a valid option. (Number from 1 to 5)')         

def addNewContact(contactList):
    print("Let's to add your contact")
    contactName = input('First name and last name ').lower()
    contactEmail = input('Email ')
    contactPhoneNumber = input('Phone number ')
    contactList[contactName] = {'contactPhoneNumber': contactPhoneNumber, 'contactEmail': contactEmail}
    print('Contact added successfully!')


def removeContact(contactList):
    print("Let's to remove a contact")
    contactName = input('First name and last name').lower()
    if contactName in contactList:
        del contactList[contactName]
        print('Contact removed successfully!')
    else:
        print(f"There's no a contact with the name {contactName}")

def searchContact(contactList):
    print("Let's to search a contact")
    contactName = input('First name and last name ')
    print('')
    if contactName in contactList:
        print(f'Name: {contactName}')
        print(f"Phone number: {contactList[contactName]['contactPhoneNumber']}")
        print(f"Email: {contactList[contactName]['contactEmail']}")
    else:
        print(f"There's no a contact with the name {contactName}")


def showContactList(contactList):
    if contactList: #Not empty
        print('Contact list: ')
        print('')
        for contactName, contactInfo in contactList.items():
            print(f'Name: {contactName}')
            print(f"Phone number: {contactInfo['contactPhoneNumber']}")
            print(f"Email: {contactInfo['contactEmail']}")
            print('-' * 20)
    else:
        print('The contact list is empty')

Main()