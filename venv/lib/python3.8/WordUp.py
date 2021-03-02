# Serena Paley
# March, 2021
from getpass import getpass


def main():

    print('Welcome to Word Up')
    secret_word = getpass('Enter the secret word')
    current_list = ["_"] * len(secret_word)

    while "_" in current_list:
        print_board(current_list)
        print()
        guess_letter()


def print_board(current_list):
    for i in current_list:
        print(i, end=" ")


def guess_letter():
    guess = input("Guess a letter ")
    return guess


if __name__ == "__main__":
    main()