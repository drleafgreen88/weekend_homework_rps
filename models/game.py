# from random import choices
from models.player import *

class Game():
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = ""


def new_game(self):
    if self.player1.choice == self.player2.choice:
        self.result = "Both players selected the same. It's a draw!"
    elif self.player1.choice == "rock":
        if self.player2.choice == "scissors":
            self.result = "Player 1 wins by playing rock."
        else:
            self.result = "Player 2 wins by playing paper."
    elif self.player1.choice == "paper":
        if self.player2.choice == "rock":
            self.result = "Player 1 wins by playing paper."
        else:
            self.result = "Player 2 wins by playing scissors."
    elif self.player1.choice == "scissors":
        if self.player2.choice == "paper":
            self.result = "Player 1 wins by playing scissors."
        else:
            self.result = "Player 2 wins by playing rock."




# def new_game(game):
#     if player_1 == player_2:
#     print(f"Both players selected {player_1}. It's a tie!")
# elif player1 == "rock":
#     if computer_action == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif user_action == "paper":
#     if computer_action == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif user_action == "scissors":
#     if computer_action == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")