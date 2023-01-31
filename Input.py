from random import *

def ghostGame(localScore):
    score = localScore
    ghost_door = randint(1,3)
    usersel = input("There are Three Doors Ahead. \nA Ghost is behind one of the doors. \nPick a door: ")
    if (usersel == str(ghost_door)):
        score += 1
        print("Good Job! Your score is now " + str(score))
        ghostGame(score)
    elif usersel == "end":
        print("Thanks for playing! Your Final Score was " + str(score))
        start();
    elif usersel != "1" and usersel != "2" and usersel != "3" and usersel != "end":
        print("Invalid Syntax. Enter 1, 2, or 3, or alternatively end to end the game.")
        ghostGame(score)
    else:
        print("Nice Try! You selected Door " + usersel + ", and the door was " + str(ghost_door) + ". Score is still " + str(score))
        ghostGame(score)

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def calc():
    num1In = input("Enter First Number: ")
    if isFloat(num1In) == False:
        print("ERROR: Numbers need to be numbers")
        calc()
        
    num2In = input("Enter Second Number: ")
    if isFloat(num2In) == False:
        print("ERROR: Numbers need to be numbers")
        calc()
        
    num1 = float(num1In)
    num2 = float(num2In)

    operator = input("Add, Subtract, Multiply, or Divide? ")

    if operator.lower() == "add" or operator.lower() == "a" or operator.lower() == "+":
        print(num1 + num2)
    elif operator.lower() == "subtract" or operator.lower() == "sub" or operator.lower() == "s" or operator.lower() == "-":
        print(num1 - num2)
    elif operator.lower() == "multiply" or operator.lower() == "mul" or operator.lower() == "m" or operator.lower() == "*":
        print(num1 * num2)
    elif operator.lower() == "divide" or operator.lower() == "div" or operator.lower() == "d" or operator.lower() == "/":
        print(num1 / num2)

    start()

def start():
    usage = input("What Tool are you using? ")

    if (usage.lower() == "calc" or usage.lower() == "calculator"):
        calc();
    elif (usage.lower() == "gg" or usage.lower() == "ghost game" or usage.lower() == "ggame" or usage.lower() == "ghostgame"):
        print("Putz Ghost Game.")
        ghostGame(0)
    else:
        print("Invalid Tool. Options are:\nCalculator - 'calc' or 'calculator\nGhost Game - 'gg' or 'ghost game' or 'ggame' or 'ghostgame'")
        start()


start()
