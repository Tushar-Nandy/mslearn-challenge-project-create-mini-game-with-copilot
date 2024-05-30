#import all the necessary libraries for rock paper siccors games
#in this there's a player and a computer, each chooses either rock, paper or siccors and the winner is decided based on the rules of the game
#rock beats siccors, siccors beats paper and paper beats rock
#the game is played until the player decides to quit
#the player can also see the score of the game

import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    player_score = 0
    computer_score = 0
    while True:
        clear()
        print("Rock, Paper, Siccors")
        print("Player: {} Computer: {}".format(player_score, computer_score))
        print("Choose your weapon!")
        print("[1] Rock")
        print("[2] Paper")
        print("[3] Siccors")
        print("[4] Quit")
        player_choice = input()
        if player_choice == "4":
            break
        computer_choice = random.randint(1, 3)
        if player_choice == "1":
            if computer_choice == 1:
                print("Computer chose Rock. It's a tie!")
            elif computer_choice == 2:
                print("Computer chose Paper. Computer wins!")
                computer_score += 1
            else:
                print("Computer chose Siccors. Player wins!")
                player_score += 1
        elif player_choice == "2":
            if computer_choice == 1:
                print("Computer chose Rock. Player wins!")
                player_score += 1
            elif computer_choice == 2:
                print("Computer chose Paper. It's a tie!")
            else:
                print("Computer chose Siccors. Computer wins!")
                computer_score += 1
        elif player_choice == "3":
            if computer_choice == 1:
                print("Computer chose Rock. Computer wins!")
                computer_score += 1
            elif computer_choice == 2:
                print("Computer chose Paper. Player wins!")
                player_score += 1
            else:
                print("Computer chose Siccors. It's a tie!")
        else:
            print("Invalid choice. Please choose a valid option.")
            continue
        input("Press Enter to continue...")
    print("Final Score:")
    print("Player: {} Computer: {}".format(player_score, computer_score))

if __name__ == '__main__':
    game()

