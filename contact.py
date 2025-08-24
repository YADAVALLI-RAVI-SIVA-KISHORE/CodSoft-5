contacts={}
def add_cont():
    name=input('Enter Name : ')
    number=input('Enter Phone Number : ')
    email=input('Enter Email : ')
    address=input('Enter Address : ')
    contacts[name]={'Phone Number':number,'Email':email,'Address':address}
    print('Contact added successfully !')
def view_cont():
    if not contacts:
        print('No contacts are available !')
    else:
        for name,details in contacts.items():
            print(f'\nName : {name}')
            for key,value in details.items():
              print(f'{key} : {value}')
def search_cont():
    search=input('Enter the name or phone number to search : ')
    for name,details in contacts.items():
        if search==name or search==details['Phone Number']:
            print(f'\nName : {name}')
            for key,value in details.items():
                print(f'{key} : {value}')
            return
    print('Your search contact was not found !')
def update_cont():
    name=input('Enter the name of contact that  you want to update : ')
    if name in contacts:
        phone=input('Enter new Phone Number : ')
        email=input('Enter new Email : ')
        address=input('Enter new Address: ')
        contacts[name]={'Phone Number':phone,'Email':email,'Address':address}
        print('Your contact successfully updated !')
    else:
        print('Contact not found !')
def delete_cont():
    name=input('Enter the name of contact that you want to delete : ')
    if name in contacts:
        del contacts[name]
        print('Contact deleted successfully !')
    else:
        print('Contact not found !')
while True:
    print('---------- Contact Book ----------')
    print('1.Add Contact')
    print('2.View Contacts')
    print('3.Search Contact')
    print('4.Update Contact')
    print('5.Delete Contact')
    print('6.Exit')
    choice=int(input('Choose (1-6) : '))
    if choice==1:
        add_cont()
    elif choice==2:
        view_cont()
    elif choice==3:
        search_cont()
    elif choice==4:
        update_cont()
    elif choice==5:
        delete_cont()
    elif choice==6:
        print("Goodbye.....")
        break
    else:
        print('Invalid choice try again !')
