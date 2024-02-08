# Rock-Paper-Scissors Game
# Code a game of rock paper scissors.

# Instructions
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
from random import randint

def get_hand(mudra):
    hand = "exit"
    if mudra == "0":
        hand = "Rock"
    elif mudra == "1":
        hand = "Scissors"
    elif mudra == "2":
        hand = "Paper"
    return hand

def determine_winner(player1, player2):
    print(f"\n     You played:   {player1}\nComputer played:   {player2}")

    if (player1 == "Rock" and player2 == "Rock") or (player1 == "Paper" and player2 == "Paper") or (player1 == "Scissors" and player2 == "Scissors"):
        print("                   Its a tie")

    elif (player1 == "Paper" and player2 == "Rock") or (player1 == "Scissors" and player2 == "Paper") or (player1 == "Rock" and player2 == "Scissors"):
        print("                   You Won!")

    elif (player1 == "Scissors" and player2 == "Rock") or (player1 == "Paper" and player2 == "Scissors") or (player1 == "Rock" and player2 == "Paper"):
        print("                   You Lost!")

user_hand = get_hand(input("Enter a number between 0-2. Or 'exit' to quit: ")) 

while user_hand.lower() != "exit":
    computer_hand = get_hand(str(randint(0,2)))

    determine_winner(user_hand, computer_hand)
    user_hand = get_hand(input("\nEnter a number between 0-2. Or any other number to quit: ")) 

  