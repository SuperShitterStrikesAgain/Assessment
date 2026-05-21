# imports
import random
# Definings
def instructions():
    # instructions
    makestat("Welcome to the Math quiz!")
    makestat("You will have a number of attempts to answer the question correctly.")
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

def questionmakertimes(roundsright,roundswrong):

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
        if userans == answer:
            # if first and correct, print then break
            print("Correct!")
            roundsright += 1
            return roundsright
        elif userans is not answer:
            # if wrong, tell answer and break
            print(f"Incorrect! the answer was {answer}!")
            roundswrong += 1
            return roundswrong

def questionmakerdiv(roundsright,roundswrong):
    # same as above, only minor changes
    # gens numbers
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 12)
    # question setup

    # intcheck setup
    userans = intcheck(f"What is {number1} divided by {number2}, rounded down?")
    # ans setup
    answer = number1 // number2
    # loooooop
    while True:
        if userans == answer:
            # if first and correct, print then break
            print("Correct!")
            roundsright += 1
            return roundsright
        elif userans is not answer:
            # if wrong, tell answer and break
            print(f"Incorrect! the answer was {answer}!")
            roundswrong += 1
            return roundswrong

def questionmakerplus(roundsright,roundswrong):
    # gens numbers
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    # question setup

    # intcheck setup
    userans = intcheck(f"What is {number1} plus {number2}?")
    # ans setup
    answer = number1 + number2
    # loooooop
    while True:
        if userans == answer:
            # if first and correct, print then break
            print("Correct!")
            roundsright += 1
            return roundsright
        elif userans is not answer:
            # if wrong, tell answer and break
            print(f"Incorrect! the answer was {answer}!")
            roundswrong += 1
            return roundswrong

def questionmakerminus(roundsright,roundswrong):
    # gens numbers
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    # question setup

    # intcheck setup
    userans = intcheck(f"What is {number1} - {number2}?")
    # ans setup
    answer = number1 - number2
    # loooooop
    while True:
        if userans == answer:
            # if first and correct, print then break
            print("Correct!")
            roundsright += 1
            return roundsright
        elif userans is not answer:
            # if wrong, tell answer and break
            print(f"Incorrect! the answer was {answer}!")
            roundswrong += 1
            return roundswrong

def mathtypecheck(question,validmath=("m","1","mu","mul","mult","multi","multip","multipl","multiplic","multiplca","multiplicat","multiplicati","multiplicatio","multiplication","times","d","2","mu","div","divi","divis","divisi","divisio","division","divide","a","3","ad","add","addi","addit","additi","additio","addition","plus","s","4","su","sub","subt","subtr","subtra","subtrac","subtract","subtracti","subtractio","subtraction","minus")):
    # setup
    error3 = "Please enter a mathmatics type. (Multiplication, Division, Addition, Subtraction)"
    while True:

        # Get user response
        to_check1 = input(question).lower()

        for item in validmath:
            # check if the user response in a word in the list
            if item == to_check1:
                return item

            # check if the user response is valid
            elif to_check1 == item[0]:
                print()
                print(error3)
                return item

def mathquestiondecider():
    while True:
        try: # checks if there is a mathtype + uses def for the one chosen
            if mathtype == 1:
                (questionmakertimes(roundscorrect,roundsincorrect))
                return mathtype
            if mathtype == 2:
                (questionmakerdiv(roundscorrect,roundsincorrect))
                return mathtype
            if mathtype == 3:
                (questionmakerplus(roundscorrect,roundsincorrect))
                return mathtype
            if mathtype == 4:
                (questionmakerminus(roundscorrect,roundsincorrect))
                return mathtype
        except ValueError:
            print("error")

def resultgiver(response, answer):
    roundresult = "what"
    if response == answer:
        roundresult = "correct"
    elif response is not answer:
        roundresult = "incorrect"
    else:
        print("what")
    return roundresult

# loop setup
mode = "regular"
roundsplayed = 0
usermath = 0
gamehistory = []
roundscorrect = 0
roundsincorrect = 0
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
usermath = mathtypecheck("What kind of mathematics do you want to do? (Multiplication, Division, Addition, or subtraction)")

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

    historyitem = (f"Round: {roundsplayed}"
                   f" - Amount of right answers: {roundscorrect}"
                   f" - Amount of wrong answers: {roundsincorrect}")
    gamehistory.append(historyitem)

if roundsplayed > 0:
    # calculate stats
    percentright = roundscorrect / roundsplayed * 100
    percentwrong = roundsincorrect / roundsplayed * 100

    # output game stats
    print("Game Stats")
    print(f"Correct: {percentright: .2f} \t "
          f"Wrong: {percentwrong:.2f} \t ")

    # Ask user if they want to see their game history
    seehistory = yncheck("\nDo you want to see your Game History? ")
    if seehistory == "yes":
        for item in gamehistory:
            print(item)

    print()
    makestat("Thanks for playing")

else:
    makestat("Game Exited")
