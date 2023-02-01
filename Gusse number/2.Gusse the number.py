import random

# client guess a random number wiche computer generate it
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:

        guess = int(input(f"Enter your guess between 1, {x}: "))

        if guess < random_number:
            print("guess higher.")

        elif guess > random_number:
            print("guess lower")

    print(f"Congrats!! you win and guess {random_number} corecctly.")


# computer guess the number wiche clinet choose in his/her mind.
def computer_guess(x):
    min = 0
    max = x
    feedback = ''

    while feedback != 'c':
        guess = random.randint(min, max)
        feedback = input(f"Is {guess} your number type 'C'. if its low 'L', if high type 'H': ").lower()

        if feedback == 'l':
            min = guess + 1

        elif feedback == 'h':
            max = guess - 1
    print(f"wow to me, i guess {guess} corecctly :)")


if __name__ == '__main__':

    choose = int(input("1.guess number game\n2.computer guess number game\n:"))
    if choose == 1:
        guess(10)

    elif choose == 2:
        computer_guess(100)
        
    else:
        print("wrong number!")