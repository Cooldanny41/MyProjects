

while True:

    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    operator = input("Enter a operater: ")
    if operator == "Add":
        def addition(num1, num2):
            return num1 + num2
        print(addition(num1, num2))
    elif operator == "Multiply":
        def multiply(num1, num2):
            return num1 * num2
        print(multiply(num1, num2))
    elif operator == "Subtract":
        def subtract(num1, num2):
            return num1 - num2
        print(subtract(num1, num2))
    elif operator == "Divide":
        def divide(num1, num2):
            return num1 / num2
        print(divide(num1, num2))
    else: print("Invalid Operator!")

    choice = input("Try Again?(Y/N) ")
    
    if choice != "Y":
        break
