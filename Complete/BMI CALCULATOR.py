def Metric():
    h = eval(input("Enter Height in cm: "))
    w = eval(input("Enter Weight in kg: "))
    bmi = w/((h*h)*0.0001)
    bmistatus(bmi)

def English():
    h = input("Enter Height in ft: Use this format (e.g., 5 9) ").split()
    w = eval(input("Enter Weight in lb: "))
    if len(h) != 2:
        print("Invalid Input")
        English()
    ft = eval(h[0])
    inch = eval(h[1])
    all_inches = (ft*12)+inch
    bmi = (w/pow(all_inches, 2))*703
    bmistatus(bmi)

def bmistatus(bmi):
    if bmi < 18.5:
        status = "Underweight."
    elif 18.5 <= bmi < 24.9:
        status = "Normal Weight."
    elif 24.9 <= bmi < 29.9:
        status = "Overweight."
    elif bmi >= 30:
        status = "Obese."
    print("Your bmi is", format(bmi, ".2f"), "and you are", status)

def choice():
    choices = input("M for Metric \nE for english \nChoose system: ")
    if choices == 'M' or choices == 'm':
        Metric()
    elif choices == 'e' or choices == 'E':
        English()
    else:
        choice()

def main():
    Start = input("Use BMI Calculator? y/n: ")
    if Start == 'y' or Start == 'Y':
        choice()
    elif Start =='n' or Start == 'N':
        print('Exiting...')
    elif Start == 'exit':
        print("Exiting...")
    else:
        main()

main()