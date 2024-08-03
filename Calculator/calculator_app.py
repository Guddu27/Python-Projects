
def Calculator():
    print("\n---------- Welcome to Calculator ----------\n")

    num1 = float(input("Enter the first number : "))    #Accepts first number
    num2 = float(input("\nEnter the second number : ")) #accepts second number


    while True:

        operation = int(input("\nEnter :\n1-Addition\n2-Substraction\n3-Multiplication\n4-Division\n5-Re-Enter values\n6-Exit\n\n>>>"))

        if operation == 1:
            add = num1 + num2
            print(f"Addition of {num1} + {num2} = {add}\n")   #performing Addition operation
        
        elif operation == 2:
            sub = num1 - num2
            print(f"Substraction of {num1} - {num2} = {sub}\n")     #performing Substraction operation

        elif operation == 3:
            mul = num1 * num2
            print(f"Multiplication of {num1} X {num2} = {mul}\n")   #performing Multiplication operation

        elif operation == 4:
            div = num1 / num2
            print(f"Division of {num1} ÷ {num2} = {div}\n")     #performing Division operation

        elif operation == 5:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("\nEnter the second number : "))     #Re-entering values

        elif operation == 6:
            print("Exiting Calculator App...\n")    #Exiting the app...
            break

        else:
            print("Invalid Input !!")

Calculator()

