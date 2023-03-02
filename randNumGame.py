import math;
import random;

num = random.randint(1, 10);

print("Number Guess Game!\n\n\nThe computer picked a random integer from 1 to 10.");

def calcGuessNum(guessNum):
    if (guessNum > 5):
        print("You Lost!");
        playAgain = input("\n\n\nPlay again? ");
        finish(playAgain);
    elif (guessNum > 1):
        print("Try again!")
        guess(guessNum);

def finish(playAgain):
    if (playAgain.lower() == "y" or playAgain.lower() == "yes"):
        print("\n\n\nNumber Guess Game!\n\n\nThe computer picked a random integer from 1 to 10.");
        guess(1);
    elif(playAgain.lower() == "n" or playAgain.lower() == "no"):
        print("\nThanks for playing!");
    else:
        print("Invalid input!\nTry again!\nValid inputs are: yes, y, no, n\n");
        playAgain = input("\n\nPlay again? ");
        finish(playAgain);

def guess(guessNum):
    userNum = input("\nGuess the number now! ")
    if (userNum.isdigit() == False):
        print("That's not an integer! Try again!\n");
        guess();
    elif (int(userNum) > 10 or int(userNum) < 1):
        print("That's not between 1 and 10! Try again!\n")
        guess();
    else:
        if (int(userNum) != num):
            print("Nice try, but that wasn't the number!")
            guessNum += 1;
            calcGuessNum(guessNum);
        else:
            playAgain = input("Congradulations! You win!\n\nPlay again? ");
            finish(playAgain);
                

guess(1);
