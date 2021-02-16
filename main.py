# Periodic Table Quizzer
# Made by Josh and Sam

import random
import os
import sys

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CCYAN = '\033[36m'
BOLD = '\033[01m'
RESET = '\033[0m'


counter = 0
S = {"1": "H",
    "3": "Li", 
    "4": "Be",
    "11": "Na",
    "12": "Mg", 
    "19": "K",
    "20": "Ca",
    "37": "Rb",
    "38": "Sr",
    "55": "Cs",
    "56": "Ba",
    "87": "Fr",
    "88": "Ra"}

P = {"5": "B",
    "6": "C",
    "7": "N",
    "8": "O",
    "9": "F",
    "10": "Ne",
    "13": "Al",
    "14": "Si",
    "15": "P",
    "16": "S",
    "17": "Cl",
    "18": "Ar",
    "31": "Ga",
    "32": "Ge",
    "33": "As",
    "34": "Se",
    "35": "Br",
    "36": "Kr"

}

args = sys.argv.pop(0)
CHOICES = {"P": P, "S": S}

main = {}

if len(sys.argv) == 0:
    main = S
else:
    for a in sys.argv:
        main = main | CHOICES[a]


while True:
    os.system("clear")

    if (random.randint(0,1)):
        b = random.randint(0,len(S)-1)

        que, ans = random.choice(list(main.items()))


        inp = input("Element %s(%s%s%s%s)%s: " % (CCYAN, BOLD, que, RESET, CCYAN, RESET))
    else:
        ans, que = random.choice(list(main.items()))
        inp = input("Number %s(%s%s%s%s)%s: " % (CYELLOW, BOLD, que, RESET, CYELLOW, RESET))
 
    while inp == "":
        inp = input("Please enter a non empty answer: ")
    if inp == ans:
        counter += 1
        print("%sCorrect! (%s%d so far%s%s) %s" % (CGREEN, BOLD, counter, RESET, CGREEN, RESET))
    else:
        print("%sWrong! The answer was %s%s%s%s%s%s, your score was %s%s%s%s.%s" % (CRED, BOLD, ans, RESET, CRED, RESET, CRED, BOLD, counter, RESET, CRED, RESET))
        counter = 0

    input("")
    
