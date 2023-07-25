from sys import exit
import random
import time


# function select game mode
def game_mode():
    print("\t\t\t\t*** Guess Number ***\n* Find the relationship between numbers and guess the next one *")
    time_period(3)
    print("------------------------")
    mode = int(input("Select Game Difficulty:\n1. Normal\n2. Extreme Hard\n>> "))
    time_period(1)

    if mode == 1:
        print("* Welcome to \"Normal\" game mode *\nWe are generating the numbers ...")
        print("------------------------")
        time_period(5)
        normal_mode()

    elif mode == 2:
        print("* Welcome to \"Extreme Hard\" game mode *\nWe are generating the numbers ...")
        print("------------------------")
        time_period(5)
        Hard_mode()

    else:
        die_in("Wrong number.try later")
        time_period(3)


def create_random_number(first, factor):
    # create first number for game
    if first == 1:
        number = random.randint(6, 9)

        return number

    # create factor for hard mode
    elif factor == 1:
        number_list = [2, 4, 6]
        number = random.choice(number_list)

        return number

    else:
        pass


def reverse_number(number):
    rev_number = 0
    # zero count for number with zero unity
    zero_count = number % 10

    while number > 0:
        count = number % 10
        rev_number = rev_number * 10 + count
        number = number // 10

    # add 0 to reverse number
    if zero_count == 0:
        rev_number = '0' + str(rev_number)

    else:
        pass

    return rev_number


# take number from client
def guess_number():
    guess = input(f"Guess the next one:>> ")

    if guess < '0' or guess == '':
        guess = input(f"Please enter a valid number:>> ")
        print("------------------------")

        if guess < '0' or guess == '':
            die_in("Sorry, you must try again.")

        return guess

    else:
        print("------------------------")

        return guess


# count = for number in normal_mode function body, x = whenever you want to give hint
def hint(count, x, text):
    if count == x:
        choose = input("Do you need a hint?(Yes/No)\n>>")

        if choose == 'Y' or choose == 'y' or "yes":
            print(text)
            time_period(7)
            print("------------------------")

        else:
            print("------------------------")

    else:
        pass


def normal_mode():
    # count the numbers
    num_count = 1
    first_number = create_random_number(1, 0)
    print(f"Base number = {first_number}")
    base_number = first_number

    for for_count in range(0, 6):
        # generate base number
        base_number *= 3
        # reverse base number
        rev_base_number = reverse_number(base_number)
        # generate next number
        new_number = base_number * 3
        print(f"Number {num_count} = {rev_base_number}")
        # client number
        guess_num = guess_number()

        # check client number with next number
        if guess_num == str(new_number):
            print("You win.Congrats!!!")
            die_in("------------------------")
            time_period(3)

        else:
            num_count += 1

        # hint in middle of game
        hint(for_count, 2, "Check them reverse and try some \"* or / or + or -\" between the numbers."
                           "\n(* remember use the calculator. *)")

        # if statement for finish the game
        if for_count == 5:
            print("You lose the game.\nThis is the solution: Reverse the number and Multiply it by 3.")
            time_period(5)

        else:
            pass


def Hard_mode():
    # count the numbers
    num_count = 2
    first_number = create_random_number(1, 0)
    print(f"Number 1 = {first_number}")
    base_number = first_number
    # factor: for multiply numbers
    factor = create_random_number(0, 1)

    for for_count in range(0, 6):
        # generate base number
        base_number *= factor
        # reverse base number
        rev_base_number = reverse_number(base_number)
        # generate next number
        new_number = base_number * factor
        print(f"Number {num_count} = {rev_base_number}", end='')
        # made 15 seconds timer and after the timer we hide the base number
        timer(7)
        # client number
        guess_num = guess_number()
        show_factor = factor

        # check client number with next number
        if guess_num == str(new_number):
            print("You win.Congrats!!!")
            die_in("------------------------")

        else:
            # hint in middle of game
            hint(for_count, 2, "Check them reverse and try some \"* or / or + or -\" between the numbers."
                               "\n(* remember use the calculator. *)")
            print(f"Number {num_count} = {rev_base_number}")
            num_count += 1

        # if statement for finish the game
        if for_count == 5:
            print(f"You loose the game.\nThis is the solution: Reverse the number and Multiply it by {show_factor}.")
            time_period(5)

        else:
            pass


def timer(second):
    print("\t\tTimer:", end='')

    # made count down
    while second:
        print(f"{second},", end='')
        time.sleep(1)
        second -= 1

        #  timer finish
        if second == 0:
            print("\rtime out.")

        else:
            pass


# made a few seconds sleep in output
def time_period(seconds):
    time.sleep(seconds)


# exit function
def die_in(text):
    print(text)
    exit(0)


if __name__ == '__main__':
    game_mode()
