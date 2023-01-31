import math;
from random import *;
import random;
from math import *;

rock = 1;
paper = 2;
scissors = 3;

def RPS(localScore, compScoreIn):
    score = localScore;
    compScore = compScoreIn;
    rps = randint(1,3);
    userNum = 0;
    userStr = "";
    if (rps == 1):
        compStr = "Rock";
    elif (rps == 2):
        compStr = "Paper";
    else:
        compStr = "Scissors"
    usersel = input("Rock, Paper, or Scissors? ");
    if (usersel.lower() == "rock" or usersel.lower() == "r"):
        userNum = 1;
    elif (usersel.lower() == "paper" or usersel.lower() == "p"):
        userNum = 2;
    elif (usersel.lower() == "scissors" or usersel.lower() == "s"):
        userNum = 3;
    else:
        print("ERROR: You must input Rock, r, Paper, p, Scissors, or s.\nIf you wish to end the game simply type end.");
        RPS(score);

    gameDiff = userNum - rps;
    if (gameDiff == 1 or gameDiff == -2):
        score += 1;
        print("Good Job!\nComputer Picked: " + compStr + "\nYou picked: " + userStr +  "\nYour score is now " + str(score) + ".\nThe Computer's Score is now " + str(compScore) + ".");
        RPS(score, compScore);
    elif (gameDiff == -1 or gameDiff == 2):
        compScore += 1;
        print("Nice Try!\nComputer Picked: " + compStr + "\nYou picked: " + userStr +  "\nYour score is now " + str(score) + ".\nThe Computer's Score is now " + str(compScore) + ".");
        RPS(score, compScore);
    elif (gameDiff == 0):
        print("Tie!\nYour Score: " + str(score) + "\nThe Computer's Score is: " + str(compScore));
    elif usersel == "end":
        print("Thanks for playing! Your Final Score was " + str(score));

RPS(0, 0);
