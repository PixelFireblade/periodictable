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
     "36": "Kr",
     "49": "In",
     "50": "Sn",
     "51": "Sb",
     "52": "Te",
     "53": "I",
     "54": "Xe",
     "81": "Tl",
     "82": "Pb",
     "83": "Bi",
     "84": "Po",
     "85": "At",
     "86": "Rn",
     "113": "Nh",
     "114": "Fl",
     "115": "Mc",
     "116": "Lv",
     "117": "Ts",
     "118": "Og"

     }

D1= {
    "21":"Sc",
    "22":"Ti",
    "23":"V",
    "24":"Cr",
    "25":"Mn",
    "26":"Fe",
    "27":"Co",
    "28":"Ni",
    "29":"Cu",
    "30":"Zn",

}

D2= {
    "39":"Y",
    "40":"Zr",
    "41":"Nb",
    "42":"Mo",
    "43":"Tc",
    "44":"Ru",
    "45":"Rh",
    "46":"Pd",
    "47":"Ag",
    "48":"Cd",
}

D3= {
    "57":"La",
    "72":"Hf",
    "73":"Ta",
    "74":"W",
    "75":"Re",
    "76":"Os",
    "77":"Ir",
    "78":"Pt",
    "79":"Au",
    "80":"Hg",

}

D4= {
    "89":"Ac",
    "104":"Rf",
    "105":"Db",
    "106":"Sg",
    "107":"Bh",
    "108":"Hs",
    "109":"Mt",
    "110":"Ds",
    "111":"Rg",
    "112":"Cn",
}

F1 = {
    "58":"Ce",
    "59":"Pr",
    "60":"Nd",
    "61":"Pm",
    "62":"Sm",
    "63":"Eu",
    "64":"Gd",
    "65":"Tb",
    "66":"Dy",
    "67":"Ho",
    "68":"Er",
    "69":"Tm",
    "70":"Yb",
    "71":"Lu",

}

F2 = {
    "90":"Th",
    "91":"Pa",
    "92":"U",
    "93":"Np",
    "94":"Pu",
    "95":"Am",
    "96":"Cm",
    "97":"Bk",
    "98":"Cf",
    "99":"Es",
    "100":"Fm",
    "101":"Md",
    "102":"No",
    "103":"Lr",
}

args = sys.argv.pop(0)
CHOICES = {"P": P, "S": S, "D1": D1, "D2": D2, "D3": D3, "D4": D4, "F1": F1, "F2": F2}

main = {} 

if len(sys.argv) == 0:
    main = S
else:
    for a in sys.argv:
        main = main | CHOICES[a]


while True:
    os.system("clear")

    if (random.randint(0, 1)):
        b = random.randint(0, len(S)-1)

        que, ans = random.choice(list(main.items()))

        inp = input("Element %s(%s%s%s%s)%s: " %
                    (CCYAN, BOLD, que, RESET, CCYAN, RESET))
    else:
        ans, que = random.choice(list(main.items()))
        inp = input("Number %s(%s%s%s%s)%s: " %
                    (CYELLOW, BOLD, que, RESET, CYELLOW, RESET))

    while inp == "":
        inp = input("Please enter a non empty answer: ")
    if inp == ans:
        counter += 1
        print("%sCorrect! (%s%d so far%s%s) %s" %
              (CGREEN, BOLD, counter, RESET, CGREEN, RESET))
    else:
        print("%sWrong! The answer was %s%s%s%s%s%s, your score was %s%s%s%s.%s" % (
            CRED, BOLD, ans, RESET, CRED, RESET, CRED, BOLD, counter, RESET, CRED, RESET))
        counter = 0

    input("")
