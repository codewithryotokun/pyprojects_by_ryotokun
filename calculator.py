while True:
    userinput = int(input("Enter the first value for calculation: "))
    operation = input("Enter the operation (+, -, *, /): ")
    userinput2 = int(input("Enter the second value for calculation: "))

    if operation == "+":
        print("The answer is:",userinput + userinput2)
    elif operation == "-":
        print("The answer is:",userinput - userinput2)
    elif operation == "*":
        print("The answer is:",userinput * userinput2)
    elif operation == "/":
        if userinput2 != 0:
            print("The answer is:",userinput / userinput2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation")

    # Ask if the user wants to continue
    again = input("Do you want to restart the calculator? (Yes/No): ")
    if again.lower() != 'yes':
        print("Exiting calculator. Goodbye!")
    break
