running = True


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def userInputCheck(inputToCheck):
    if not isFloat(inputToCheck):
        print("ERROR: Must be an integer")
    else:
        inCheck = float(inputToCheck) - round(float(inputToCheck))
        if inCheck != 0:
            print("ERROR: Must be an integer")
        else:
            return calculate(round(float(inputToCheck)))


def calculate(userNum):
    greaterThan100 = userNum > 100
    even = userNum % 2 == 0
    if even:
        evenStr = " is even"
    else:
        evenStr = " is odd"

    if greaterThan100:
        greaterThan100Str = " is greater than 100."
    else:
        greaterThan100Str = " is less than 100."

    print(str(userNum) + evenStr + " and" + greaterThan100Str)
    print("\n\n")


while running:

    userInput = input("Please type in an integer.\n\t\t\t\t\t\t  ")

    if userInput.lower() == "exit" or userInput.lower() == "quit":

        print("Thanks for using this tool!")
        running = False

    else:

        userInputCheck(userInput)
