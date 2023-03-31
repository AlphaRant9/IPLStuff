running = True


def signum(num):
    if abs(num) == 0:
        return 0
    else:
        return num / abs(num)


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
    greaterThan25 = userNum > 25
    even = userNum % 2 == 0
    if even:
        evenStr = " is even"
    else:
        evenStr = " is odd"

    if greaterThan25:
        greaterThan25Str = " is greater than 25, you win!"
    else:
        greaterThan25Str = " is less than 25, thanks for playing!"

    print(str(userNum) + evenStr + " and" + greaterThan25Str)
    num = 1.0
    while num <= 10:
        print("Count to 10: " + str(num))
        num += 1

    num = 1.0
    while abs(num) <= abs(userNum):
        print("Count to User Num: " + str(num))
        num += 1 * signum(userNum)
    print("\n\n")


while running:

    userInput = input("Please type in an integer.\n\t\t\t\t\t\t  ")

    if userInput.lower() == "exit" or userInput.lower() == "quit":

        print("Thanks for using this tool!")
        running = False

    else:

        userInputCheck(userInput)
