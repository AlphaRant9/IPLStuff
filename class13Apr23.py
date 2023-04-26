import sys

isOperationRunning = True


def inputPayRate():

    payRateStr = input("What is your hourly pay rate? ")

    if isFloat(payRateStr):

        return float(payRateStr)

    else:

        print("ERROR: Must be a number.\n\n")
        return inputPayRate()


def inputHoursWorked():

    hoursStr = input("What is the sum of your total hours worked? ")

    if isFloat(hoursStr):

        return float(hoursStr)

    else:

        print("ERROR: Must be a number.\n\n")
        return inputPayRate()


def isFloat(num):

    try:

        float(num)
        return True

    except ValueError:

        return False


def calculateIncome():
    if hours > 40:
        otHours = hours - 40  # otHours is overtime hours
        otPayRate = payRate * 1.5  # overtime pay rate
        grossIncome = round(payRate * 40, 2) + round(otPayRate * otHours, 2)
    else:
        grossIncome = round(payRate * hours, 2)
    soSecMed = round(grossIncome * 0.0765, 2)
    stateTax = round(grossIncome * 0.05, 2)
    fedTax = round(grossIncome * 0.2, 2)
    netIncome = round(grossIncome - soSecMed - stateTax - fedTax, 2)

    print(
        f'{employeeName}\'s gross income is ${grossIncome}, and their net income is ${netIncome} after ${soSecMed}'
        f'paid for social security and medicare, ${stateTax} paid in state tax, and ${fedTax} paid in federal taxes.')


while isOperationRunning:
    
    employeeName = input("What is your name? ")

    payRate = inputPayRate()
    hours = inputHoursWorked()

    calculateIncome()

    quitStr = input("Do you want to quit? ")
    print("\n")
    if quitStr.lower() == "y" or quitStr.lower() == "yes":
        print("Thank you for using this tool!")
        isOperationRunning = False
        sys.exit()
