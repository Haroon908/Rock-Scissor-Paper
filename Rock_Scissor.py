import math
import random


def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper and 's' for scissor\n")
    user =  user.lower()

    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0,user,computer)

    if is_win(user,computer):
         return (1,user,computer)


    return (-1,user,computer)


def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):

    player_wins = 0
    computer_wins = 0
    wins_necessory = math.ceil(n%2)

    while player_wins < wins_necessory or computer_wins < wins_necessory:
        result,user,computer = play()

        if result==0:
            print(f"It is a tie, You and computer both have chosen {computer}")
        elif result== 1:
            player_wins += 1
            print(f"You won.You chose {user} and computer chose {computer}")
        else:
            computer_wins += 1
            print(f"You lost.You chose {user} and computer chose {computer}")

    if player_wins > computer_wins:
        print(f"You have won out of {n} games")
    else:
        print(f"computer has won out of {n} games")


if __name__ == '__main__':
    play_best_of(3)