import random

def play(x):
    p_score, c_score = 0 , 0

    # Conditions for win
    def is_win(player, opponent):

        if (player == 'r' and opponent == 's') or ( player == 'p' and opponent == 'r') or \
            (player == 's' and opponent == 'p'):
            return True

    # game body
    while p_score != x and c_score != x:
        player = input("\nRock 'R', paper 'P', scissors 'S': ").lower()
        computer = random.choice(['r', 'p', 's'])
        if  player == computer:
            print("tie selection.")
        
        elif is_win(player, computer):
            p_score += 1
            print("score for you.")
        
        elif is_win(computer, player):
            c_score += 1
            print("score for computer.")

    # print for winner
    if p_score == x :
        print("Congrats, you win this game.")

    elif c_score == x :
        print("Sorry but computer win this one, try again.")

if __name__ == "__main__":
    play(3) 