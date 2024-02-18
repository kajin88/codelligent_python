while True:
    print("*" * 30)
    print("SIMPLE CALCULATOR")
    print("*" * 30)
    print("1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
    print("-" * 30)
    choice = int(input("Please enter your option: "))

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Sum is ", num1 + num2)
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Difference is ", num1 - num2)
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Product is ", num1 * num2)
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Result is ", num1 / num2)
    elif choice == 5:
        break
    else:
        print("Sorry, wrong input!")