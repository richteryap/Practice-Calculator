def addition(number1, number2):
    print(f"{number1} + {number2} is {number1 + number2}")

def subtraction(number1, number2):
    print(f"{number1} - {number2} is {number1 - number2}")

def multiplication(number1, number2):
    print(f"{number1} x {number2} is {number1 * number2}")

def division(number1, number2):
    print(f"{number1} / {number2} is {number1 / number2}")

def Calculator():
    solution = input("").split()
    if len(solution) != 3:
        print("Invalid Input")
        Calculator()

    number1 = eval(solution[0])
    operation = solution[1]
    number2 = eval(solution[2])

    if operation == '+':
        addition(number1, number2)
    elif operation == '-':
        subtraction(number1, number2)
    elif operation == '*':
        multiplication(number1, number2)
    elif operation == '/':
        division(number1, number2)
    else:
        print("Invalid Sign Input")
        Calculator()

def main():
    enter = input("Do you want to use the Basic Calculator? y/n: ")
    if enter == 'y' or enter == 'Y':
        print("---BASIC CALCULATOR---")
        print("Use this format: 1 + 1")
        Calculator()
    if enter == 'n' or enter == 'N':
        print("Exiting...")
    else:
        main()

main()