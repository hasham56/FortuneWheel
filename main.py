import turtle
from turtle import *
import random
from time import time


def load_phrase():  # Function to load all phrases from the file and return a random phrase.
    try:
        phrases_file = open('WofFPhrases.txt')
        phrases_list = phrases_file.readlines()
        phrases_file.close()

        for index in range(len(phrases_list)):
            phrases_list[index] = phrases_list[index][0:-1]

        random_phrase = phrases_list[random.randint(0, len(phrases_list) - 1)]
        return random_phrase

    except FileNotFoundError:
        print('Phrases File Not Found')


def create_boxes(random_phrase):  # Function to create boxes for letters using turtle.
    draw_turtle.penup()
    if len(random_phrase) >= 50:
        draw_turtle.backward(470)
    elif 50 > len(random_phrase) >= 45:
        draw_turtle.backward(430)
    elif 45 > len(random_phrase) >= 40:
        draw_turtle.backward(390)
    elif 40 > len(random_phrase) >= 35:
        draw_turtle.backward(350)
    elif 35 > len(random_phrase) >= 30:
        draw_turtle.backward(310)
    elif 30 > len(random_phrase) >= 25:
        draw_turtle.backward(270)
    elif 25 > len(random_phrase) >= 20:
        draw_turtle.backward(230)
    elif len(random_phrase) < 20:
        draw_turtle.backward(190)
    draw_turtle.right(90)
    draw_turtle.forward(200)
    draw_turtle.left(90)

    for character in random_phrase:
        if character != ' ':
            draw_turtle.pendown()
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.penup()
            draw_turtle.forward(20)

        elif character == ' ':
            draw_turtle.penup()
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.forward(15)
            draw_turtle.left(90)
            draw_turtle.penup()
            draw_turtle.forward(20)

    draw_turtle.backward(len(random_phrase)*20)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Initializing the Turtle ----------------------------------------------


screen = Screen()
screen.title('Fortune Wheel')
screen.bgcolor('white')
screen.setup(width=1030, height=600)
for x in range(0, 24):
    screen.register_shape(f'wheels/wheel{x}.gif')

wheel = turtle.Turtle()
wheel.shape('wheels/wheel0.gif')
wheel.shapesize(1, 1, 1)
wheel.penup()
wheel.left(90)
wheel.forward(50)
wheel.right(90)

pointer = turtle.Turtle()
pointer.color('red', 'yellow')
pointer.speed(0)
pointer.pensize(2)
pointer.hideturtle()
pointer.speed(0)
pointer.penup()
pointer.left(90)
pointer.forward(200)
pointer.left(90)
pointer.forward(20)
pointer.right(180)
pointer.pendown()
pointer.begin_fill()
pointer.forward(40)
pointer.right(120)
pointer.forward(40)
pointer.right(120)
pointer.forward(40)
pointer.end_fill()

draw_turtle = turtle.Turtle()
draw_turtle.color('#003366')
draw_turtle.pensize(2)
draw_turtle.hideturtle()
draw_turtle.speed(0)

r_phrase = load_phrase()


def spin():
    for _ in range(8):
        for x in range(0, 24):
            wheel.shape(f'wheels/wheel{x}.gif')

    value = random.randint(0, 23)
    wheel.shape(f'wheels/wheel{value}.gif')
    return value


def update_balance():
    print(f'Player 1: {player_1_balance} $\t\t\t\tPlayer 2: {player_2_balance} $\t\t\t\tPlayer 3: {player_3_balance} $')


player_1_balance = 0
player_2_balance = 0
player_3_balance = 0

player_1_turn = True  # First turn for player 1.
player_2_turn = False
player_3_turn = False

spin_wheel_list = [5000, 'BANKRUPT', 300, 500, 450, 500, 800, 'LOSE A TURN', 700, 'FREE PLAY', 650, 'BANKRUPT', 900,
                   500, 350, 600, 500, 400, 550, 800, 300, 700, 900, 500]

letters_guessed_list = []


def enter_consonant(spin_option):  # Function to get consonants.
    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance
    global letters_guessed_list

    start = time()
    if player_1_turn:
        check = True
        while check:
            consonant = input('Enter a Consonent: ')
            end = time()
            if int(end-start) < 10:
                if not consonant.isalpha():
                    print('Error! ', 'Please Enter An Alphabet!')
                elif len(consonant) > 1:
                    print('Error! ', 'Please Enter One Alphabet!')
                elif consonant.capitalize() == 'A' or consonant.capitalize() == 'E' or consonant.capitalize() == 'I' or consonant.capitalize() == 'O' or consonant.capitalize() == 'U':
                    print('Error! ', 'Can Not Select A Vowel!')
                elif consonant.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')
                elif consonant.capitalize() in r_phrase:
                    print('Alphabet Added in Phrase!')
                    letters_guessed_list.append(consonant.capitalize())
                    draw_letters(consonant.capitalize())
                    number_of_consonants = r_phrase.count(consonant.capitalize())
                    money_earned = number_of_consonants * spin_option
                    print('Money Earned! ', 'Player 1 Earned ${}.'.format(money_earned))
                    player_1_balance += money_earned
                    options()
                    check = False

                else:
                    money_earned = spin_option
                    print('The Selected Consonant is Not in the Phrase!')
                    print(f'Player 1 Earned only ${money_earned}!')
                    player_1_balance += money_earned
                    next_player()
                    check = False
            else:
                print('Time Up!')
                next_player()
                check = False

    elif player_2_turn:
        check = True
        while check:
            consonant = input('Enter a Consonant: ')
            end = time()
            if int(end - start) < 10:
                if not consonant.isalpha():
                    print('Error! ', 'Please Enter An Alphabet!')
                elif len(consonant) > 1:
                    print('Error! ', 'Please Enter One Alphabet!')
                elif consonant.capitalize() == 'A' or consonant.capitalize() == 'E' or consonant.capitalize() == 'I' or consonant.capitalize() == 'O' or consonant.capitalize() == 'U':
                    print('Error! ', 'Can Not Select A Vowel!')
                elif consonant.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')
                elif consonant.capitalize() in r_phrase:
                    print('Alphabet Added in Phrase!')
                    letters_guessed_list.append(consonant.capitalize())
                    draw_letters(consonant.capitalize())
                    number_of_consonants = r_phrase.count(consonant.capitalize())
                    money_earned = number_of_consonants * spin_option
                    print('Money Earned! ', 'Player 2 Earned ${}.'.format(money_earned))
                    player_2_balance += money_earned
                    options()
                    check = False

                else:
                    money_earned = spin_option
                    print('The Selected Consonant is Not in the Phrase!')
                    print(f'Player 2 Earned only ${money_earned}!')
                    player_2_balance += money_earned
                    next_player()
                    check = False
            else:
                print('Time Up!')
                next_player()
                check = False

    elif player_3_turn:
        check = True
        while check:
            consonant = input('Enter a Consonant: ')
            end = time()
            if int(end - start) < 10:
                if not consonant.isalpha():
                    print('Error! ', 'Please Enter An Alphabet!')
                elif len(consonant) > 1:
                    print('Error! ', 'Please Enter One Alphabet!')
                elif consonant.capitalize() == 'A' or consonant.capitalize() == 'E' or consonant.capitalize() == 'I' or consonant.capitalize() == 'O' or consonant.capitalize() == 'U':
                    print('Error! ', 'Can Not Select A Vowel!')
                elif consonant.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')
                elif consonant.capitalize() in r_phrase:
                    print('Alphabet Added in Phrase!')
                    letters_guessed_list.append(consonant.capitalize())
                    draw_letters(consonant.capitalize())
                    number_of_consonants = r_phrase.count(consonant.capitalize())
                    money_earned = number_of_consonants * spin_option
                    print('Money Earned!  ', 'Player 3 Earned ${}.'.format(money_earned))
                    player_3_balance += money_earned
                    options()
                    check = False

                else:
                    money_earned = spin_option
                    print('The Selected Consonant is Not in the Phrase!')
                    print(f'Player 3 Earned only ${money_earned}!')
                    player_3_balance += money_earned
                    next_player()
                    check = False
            else:
                print('Time Up!')
                next_player()
                check = False

def options():
    check = True
    option = 0
    while check:
        try:
            option = int(input('You got 3 options: 1(Spin Again), 2(Buy Vowel), 3(Solve Puzzle): '))
        except:
            print('Only Intergers are allowed!')
        if 3 < int(option) <= 0:
            print('Wrong Option')
        elif option == 1:
            spin_wheel()
            check = False
        elif option == 2:
            buy_vowel()
            check = False
        elif option == 3:
            solve_puzzle()
            check = False


def next_player():  # Function to go to next player after 10 secs.
    global player_1_turn, player_2_turn, player_3_turn

    if player_1_turn:
        player_1_turn = False
        player_2_turn = True
        player_3_turn = False

    elif player_2_turn:
        player_1_turn = False
        player_2_turn = False
        player_3_turn = True

    elif player_3_turn:
        player_1_turn = True
        player_2_turn = False
        player_3_turn = False


def spin_wheel():  # Function to spin the wheel.
    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance

    value = spin()
    spin_option = spin_wheel_list[value]
    print('\t\t\t\t\t\t\tSpin Result: ', spin_option)

    if type(spin_option) == int:
        enter_consonant(spin_option)

    elif type(spin_option) == str:
        if spin_option == 'BANKRUPT':
            print('Bankrupt! ', 'You Lost All Your Balance and Current Turn!')

            if player_1_turn:
                player_1_balance = 0

            elif player_2_turn:
                player_2_balance = 0

            elif player_3_turn:
                player_3_balance = 0
            next_player()

        elif spin_option == 'LOSE A TURN':
            print('You Lost Your Current Turn!')
            next_player()

        elif spin_option == 'FREE PLAY':
            freeplay()


def freeplay():  # Function to take free play input.
    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance
    global letters_guessed_list

    start = time()
    if player_1_turn:
        check = True
        while check:
            freeplay_input = input('Its a FreePlay enter any Letter: ')
            end = time()
            if int(end - start) < 10:
                if not freeplay_input.isalpha():
                    print('Error! ', 'Please Input an Alphabet Only!')

                elif len(freeplay_input) > 1:
                    print('Error! ', 'Please Input Only One Alphabet')

                elif freeplay_input.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')

                elif freeplay_input.capitalize() in r_phrase:
                    print('Alphabet Added to Phrase!')
                    letters_guessed_list.append(freeplay_input.capitalize())
                    draw_letters(freeplay_input.capitalize())
                    next_player()
                    check = False

                else:
                    print('Alphabet Not in the Phrase! Try Again')
                    freeplay()
            else:
                print('Time Up!')
                next_player()
                check = False

    elif player_2_turn:
        check = True
        while check:
            freeplay_input = input('Its a FreePlay enter any Letter: ')
            end = time()
            if int(end - start) < 10:
                if not freeplay_input.isalpha():
                    print('Error! ', 'Please Input an Alphabet Only!')

                elif len(freeplay_input) > 1:
                    print('Error! ', 'Please Input Only One Alphabet')

                elif freeplay_input.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')

                elif freeplay_input.capitalize() in r_phrase:
                    print('Alphabet Added to Phrase!')
                    letters_guessed_list.append(freeplay_input.capitalize())
                    draw_letters(freeplay_input.capitalize())
                    next_player()
                    check = False

                else:
                    print('Alphabet Not in the Given Phrase!')
                    next_player()
                    check = False
            else:
                print('Time Up!')
                next_player()
                check = False

    elif player_3_turn:
        check = True
        while check:
            freeplay_input = input('Its a FreePlay enter any Letter: ')
            end = time()
            if int(end - start) < 10:
                if not freeplay_input.isalpha():
                    print('Error! ', 'Please Input an Alphabet Only!')

                elif len(freeplay_input) > 1:
                    print('Error! ', 'Please Input Only One Alphabet')

                elif freeplay_input.capitalize() in letters_guessed_list:
                    print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')

                elif freeplay_input.capitalize() in r_phrase:
                    print('Alphabet Added to Phrase!')
                    letters_guessed_list.append(freeplay_input.capitalize())
                    draw_letters(freeplay_input.capitalize())
                    next_player()
                    check = False

                else:
                    print('Alphabet Not in the Given Phrase!')
                    next_player()
                    check = False
            else:
                print('Time Up!')
                next_player()
                check = False


def draw_letters(letter):  # Fucntion to fill in boxes with letters using turtle.
    position_list = [pos for pos, char in enumerate(r_phrase) if char == letter]

    for position in position_list:
        draw_turtle.penup()
        draw_turtle.forward(position * 20)

        draw_turtle.forward(4)
        draw_turtle.left(90)

        draw_turtle.pendown()
        style = ('Calibri', 11, 'bold')
        draw_turtle.write(letter, font=style)
        draw_turtle.penup()

        draw_turtle.right(90)
        draw_turtle.backward(4)

        draw_turtle.backward(position * 20)


def buy_vowel():  # Function to buy a vowel when buy vowel button pressed!
    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance
    global letters_guessed_list

    if player_1_turn:
        vowel_input = input('Enter a vowal: ')
        if player_1_balance >= 250:
            if not vowel_input.isalpha():
                print('Error! ', 'Input an Alphabet Only!')
            elif len(vowel_input) > 1:
                print('Error!', 'Input One Alphabet Only!')
            elif vowel_input.capitalize() != 'A' and vowel_input.capitalize() != 'E' and vowel_input.capitalize() != 'I' and vowel_input.capitalize() != 'O' and vowel_input.capitalize() != 'U':
                print('Error! ', 'Input a Vowel Only!')
            elif vowel_input.capitalize() in letters_guessed_list:
                print('Error! ', 'Alphabet Already Guessed, Guess Another Alphabet!')
            elif vowel_input.capitalize() in r_phrase:
                player_1_balance = player_1_balance - 250
                print('Alphabet Added to Phrase!')
                letters_guessed_list.append(vowel_input.capitalize())
                draw_letters(vowel_input.capitalize())
                options()
            else:
                print('The Chosen Alphabet is Not in the Phrase!')
                next_player()
        else:
            print("Error! ", 'Not Enough Balance to Purchase Letter!')

    elif player_2_turn:
        vowel_input = input('Enter a vowal: ')
        if player_2_balance >= 250:
            if not vowel_input.isalpha():
                print('Error!', 'Input an Alphabet Only!')
            elif len(vowel_input) > 1:
                print('Error!', 'Input One Alphabet Only!')
            elif vowel_input.capitalize() != 'A' and vowel_input.capitalize() != 'E' and vowel_input.capitalize() != 'I' and vowel_input.capitalize() != 'O' and vowel_input.capitalize() != 'U':
                print('Error!', 'Input a Vowel Only!')
            elif vowel_input.capitalize() in letters_guessed_list:
                print('Error!', 'Alphabet Already Guessed, Guess Another Alphabet!')
            elif vowel_input.capitalize() in r_phrase:
                player_2_balance = player_2_balance - 250
                print('Alphabet Added to Phrase!')
                letters_guessed_list.append(vowel_input.capitalize())
                draw_letters(vowel_input.capitalize())
                options()
            else:
                print('The Chosen Alphabet is Not in the Phrase!')
                next_player()
        else:
            print("Error!", 'Not Enough Balance to Purchase Letter!')

    elif player_3_turn:
        vowel_input = input('Enter a vowal: ')
        if player_3_balance >= 250:
            if not vowel_input.isalpha():
                print('Error!', 'Input an Alphabet Only!')
            elif len(vowel_input) > 1:
                print('Error!', 'Input One Alphabet Only!')
            elif vowel_input.capitalize() != 'A' and vowel_input.capitalize() != 'E' and vowel_input.capitalize() != 'I' and vowel_input.capitalize() != 'O' and vowel_input.capitalize() != 'U':
                print('Error!', 'Input a Vowel Only!')
            elif vowel_input.capitalize() in letters_guessed_list:
                print('Error!', 'Alphabet Already Guessed, Guess Another Alphabet!')
            elif vowel_input.capitalize() in r_phrase:
                player_3_balance = player_3_balance - 250
                print('Alphabet Added to Phrase!')
                letters_guessed_list.append(vowel_input.capitalize())
                draw_letters(vowel_input.capitalize())
                options()
            else:
                print('Alphabet Not in Phrase', 'The Chosen Alphabet is Not in the Phrase!')
                next_player()

        else:
            print("Error!", 'Not Enough Balance to Purchase Letter!')


def solve():  # Function to open a new window where player can enter the phrase.

    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance
    global letters_guessed_list

    solve_puzzle()


def solve_puzzle():  # Function to finally solve the puzzle.
    global player_1_turn, player_2_turn, player_3_turn
    global player_1_balance, player_2_balance, player_3_balance
    global letters_guessed_list

    if player_1_turn:
        solve_attempt = input('Attempt Phrase: ')
        if solve_attempt.upper() == r_phrase:
            print('You Win! ', 'Congratulations Player 1, You win ${}.'.format(player_1_balance))
            exit()
        else:
            print('Not Correct! ', 'Solution Not Correct, Turn Lost!')
            next_player()

    elif player_2_turn:
        solve_attempt = input('Attempt Phrase: ')
        if solve_attempt.upper() == r_phrase:
            print('You Win! ', 'Congratulations Player 2, You win ${}.'.format(player_2_balance))
            exit()
        else:
            print('Not Correct! ', 'Solution Not Correct, Turn Lost!')
            next_player()

    elif player_3_turn:
        solve_attempt = input('Attempt Phrase: ')
        if solve_attempt.upper() == r_phrase:
            print('You Win! ', 'Congratulations Player 3, You win ${}.'.format(player_3_balance))
        else:
            print('Not Correct! ', 'Solution Not Correct, Turn Lost!')
            next_player()

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Console Printing --------------------------------------------------


print('Hint: ', r_phrase)
print("\n------------------------ Welcome to Fortune Wheel ------------------------")
update_balance()
create_boxes(r_phrase)
print('----------------------------- Player One Turn -----------------------------')

while True:
    spin_wheel()
    if player_1_turn:
        update_balance()
        print('----------------------------- Player One Turn -----------------------------')

    elif player_2_turn:
        update_balance()
        print('----------------------------- Player Two Turn -----------------------------')

    elif player_3_turn:
        update_balance()
        print('----------------------------- Player Three Turn -----------------------------')
