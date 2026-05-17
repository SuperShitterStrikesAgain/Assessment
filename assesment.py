# imports
import math
import random

# Definings
def instructions():
    # instructions
    makestat("Welcome to the Math quiz!")
    makestat("You will have a number of guesses to answer the question correctly.")
    makestat("Good luck!")

def intcheck(question):
    while True:
        # setup
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        # check response, if no int error print
        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def makestat(state):
    # Statement decorator.
    ends = "⋆｡𖦹°⭒˚｡⋆"
    starts = "⋆｡°⭒˚𖦹｡⋆"
    print(f"\n{starts} {state} {ends}")

def yncheck(question, validans=('yes', 'no',)):
    error = f"Please enter a option from the following list: {validans}"

    while True:

        # Get user response
        user_response = input(question).lower()

        for item in validans:
            # check if the user response in a word in the list
            if item == user_response:
                return item

            # check if the user response is valid
            elif user_response == item[0]:
                return item

        # print error
        print(error)
        print()

def questionmakertimes():
    # sets guesses
    guessnum = 3
    currentguesses = guessnum
    # gens numbers
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 12)
    # question setup

    # intcheck setup
    userans = intcheck(f"What is {number1} x {number2}?")
    # ans setup
    answer = number1 * number2
    #loooooop
    while True:
        if currentguesses == 1:
            # if used all guesses, tell answer and break
            print(f"You've used all of your guesses! the answer was {answer}!")
            break
        elif userans == answer:
            # if first and correct, print then break
            print("First try!")
            break
        elif userans is not answer:
            # if it is wrong, minus guesses, tell amount of guesses and reprompt question
            currentguesses -=1
            print(f"Incorrect! you have {currentguesses} guesses left.{userans},{answer}")
            userans = intcheck(f"What is {number1} x {number2}?")
            if userans == answer:
                print("Correct!")
                break

def questionmakerdiv():
    # same as above, only minor changes
    guessnum = 3
    currentguesses = guessnum
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 12)
    mathquestiondiv = f"What is {number1} divided by {number2}, rounded down?"
    userans = intcheck(mathquestiondiv)
    answer = number1 // number2
    while True:
        if currentguesses == 1:
            print(f"You've used all of your guesses! the answer was {answer}!")
            break
        elif userans == answer:
            print("Correct!")
            break
        elif userans is not answer:
            currentguesses -=1
            print(f"Incorrect! you have {currentguesses} guesses left.")
            userans = intcheck(mathquestiondiv)
            if userans == answer:
                print("Correct!")
                break

def questionmakerplus():
    guessnum = 3
    currentguesses = guessnum
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    mathquestionplus= f"What is {number1} plus {number2}?"
    userans = intcheck(mathquestionplus)
    answer = number1 + number2
    while True:
        if currentguesses == 1:
            print(f"You've used all of your guesses! the answer was {answer}!")
            break
        elif userans == answer:
            print("Correct!")
            break
        elif userans is not answer:
            currentguesses -=1
            print(f"Incorrect! you have {currentguesses} guesses left.")
            userans = intcheck(mathquestionplus)
            if userans == answer:
                print("Correct!")
                break

def questionmakerminus():
    guessnum = 3
    currentguesses = guessnum
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    mathquestionminus= f"What is {number1} minus {number2}?"

    userans = intcheck(mathquestionminus)
    answer = number1 - number2
    while True:
        if currentguesses == 1:
            print(f"You've used all of your guesses! the answer was {answer}!")
            break
        elif userans == answer:
            print("Correct!")
            break
        elif userans is not answer:
            currentguesses -=1
            print(f"Incorrect! you have {currentguesses} guesses left.")
            userans = intcheck(mathquestionminus)
            if userans == answer:
                print("Correct!")
                break

def mathtypecheck(question):
    # setup
    error1 = "please enter a mathmatics type. (Multiplication, Division, Addition, Subtraction)"
    to_check1 = input(question).lower()
    while True:
        # check if answer is valid
        mathtype = 0
        if usermath in multlist:
            mathtype = 1
            return mathtype
        if usermath in divlist:
            mathtype = 2
            return mathtype
        if usermath in addlist:
            mathtype = 3
            return mathtype
        if usermath in sublist:
            mathtype = 4
            return mathtype
        else: # error print if not recognized
            print(error1)

def mathquestiondecider():
    while True:
        try:
            if mathtype == 1:
                (questionmakertimes())
                return mathtype
            if mathtype == 2:
                (questionmakerdiv())
                return mathtype
            if mathtype == 3:
                (questionmakerplus())
                return mathtype
            if mathtype == 4:
                (questionmakerminus())
                return mathtype
        except ValueError:
            print("error")

# loop setup
mode = "regular"
roundsplayed = 0
usermath = 0

# asks for instructions
wantinstructions = yncheck("do you want to see the instructions? ")

# Instructions print
if wantinstructions == "yes":
    instructions()

# Ask user for number of rounds
numrounds = intcheck("How many rounds would you like? Push <enter> for infinite mode: ")

# setup for inf mode
if numrounds == "infinite":
    mode = "infinite"
    numrounds = 5

multlist = {"m","1","mu","mul","mult","multi","multip","multipl","multiplic","multiplca","multiplicat","multiplicati","multiplicatio","multiplication","times"}
divlist = {"d","2","mu","div","divi","divis","divisi","divisio","division","divide"}
addlist = {"a","3","ad","add","addi","addit","additi","additio","addition","plus"}
sublist = {"s","4","su","sub","subt","subtr","subtra","subtrac","subtract","subtracti","subtractio","subtraction","minus"}

# asks for mathtype
usermath = input("What kind of mathematics do you want to do? (Multiplication, Division, Addition, or subtraction)")

mathtype = 0
if usermath in multlist:
    mathtype = 1
if usermath in divlist:
    mathtype = 2
if usermath in addlist:
    mathtype = 3
if usermath in sublist:
    mathtype = 4
# need to make error thing that doesn't break it

# looooop start
while roundsplayed < numrounds:

    # Rounds headings
    if mode == "infinite":
        roundsheading = f"\n Round {roundsplayed + 1} (Infinite Mode)"
    else:
        roundsheading = f"\n Round {roundsplayed + 1} of {numrounds}"

    # print round num
    print(roundsheading)
    print()
    mathquestiondecider()
    # adds roundcount and resets guesses
    roundsplayed += 1
    guessnum = 3
    # adds roundcount to inf mode
    if mode == "infinite":
        numrounds += 1