import random
def system():

    booking =[]

    print("\n---------- Welcome to Hotel Management System -----------")

    
    while True:

        option = int(input("\nEnter:\n1-Check availability\n2-Book Room\n3-View details\n4-Update Category\n5-Exit\n\n>>>"))


        list_of_rooms = [1000, 1020, 1023, 1056, 1047, 1067, 1078, 1048, 1034]
        room = [1023, 1056, 1078, 1034, 1048]
        category = ["single", "double"]


        if option == 1:

            print(f"Here is list of rooms : {list_of_rooms}")

            room_number = int(input("Enter room number you want to book : "))
            if room_number in room:
                print(f"Room number : {room_number} is available")
            else:
                print(f"Room number : {room_number} is not available please enter another...")
                room_number = int(input("Enter Room Number : "))

        elif option == 2:
            print(f"Do you want to book Room number : {room_number} ?")
            choice = input("yes / no : ")
            cost = 0
            if choice == "yes":
                print(f"Categories available : {category}")
                category_choice = input("Enter Category : ")

                if category_choice in category:
                    print(f"Selected category : {category_choice} is available")
                    print(f"Room number : {room_number} with category : {category_choice} booked sucessfully")
                    cost = 2000
                    booking.append(room_number)
                    booking.append(category_choice)
                    booking.append(cost)
                else:
                    print("Enter Proper category ...")
            else:
                print("Booking Cancelled")

        elif option == 3:
            print(f"Here's your booking details : {booking}")

        elif option == 4:
            print(f"Here's your booking detais : {booking}")
            update_booking = input("Enter what you want to update : ")

            if update_booking in booking:
                update = input("Enter what you want to update : ")
                ind = booking.index(update_booking)
                booking[ind] = update
            else:
                print("Booking details not found...")

        elif option == 5:
            print("Exiting Hotel Management System...")
            break 

system()