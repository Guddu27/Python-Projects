# Introducing ---> Contact Book

contact = {} # Empty dictionary for storing contacts

def contact_book():

    def display_contact():
        print("\nName\t\tContact Number")

        for key in contact:
            print("{}\t\t{}".format(key,contact.get(key))) #format method places the corresponding values

    while True:
        choice  = int(input("\n1.Add new contact\n2.Search contact\n3.Display contact\n4.Edit contact\n5.Delete contact\n6.Exit\n\nEnter your Choice : "))
        
        if choice == 1:
            name = input("\nEnter contact name : ")
            phone = input("\nEnter the phone number : ")
            contact[name] = phone    #key = name value = phone  

        elif choice == 2:
            search_name = input("\nEnter name to search : ")
            if search_name in contact:
                print("\nContact found!!")
                print(f"\n>>> {search_name}'s contact number: {contact[search_name]}")
            else:
                print("\nName not found in the contact book!")

        elif choice == 3:
            if not contact:
                print("\nContact book is empty!")
            else:
                display_contact()

        elif choice == 4:
            edit_contact = input("\nEnter contact to edit : ")
            if edit_contact in contact:
                new_contact = input("\nEnter new contact : ")
                contact[edit_contact] = new_contact #replace the new_contact with edit_contact in the dictionary
                print("\nContact Updated Successfully!")
                display_contact()
            else:
                print("\nContact now found in the contact book!")

        elif choice == 5:
            delete_contact = input("\nEnter the contact you want to delete: ")
            if delete_contact in contact:
                confirm = input("\nAre you sure you want to delete this contact y/n ? ")
                if confirm == 'y' or confirm == 'Y':
                    contact.pop(delete_contact)
                    print(f"\nContact : {delete_contact} was successfully deleted!")
                    display_contact()
                else:
                    print("\nContact deletion cancelled!")
            else:
                print(f"\nContact : {delete_contact} was not found in the contact book!")

        elif choice == 6:
            print("\nExiting Contact Book...")
            break

contact_book()


